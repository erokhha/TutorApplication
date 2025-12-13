package com.example.tutorhammer.ui.tutor.lessons

import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/* ---------------- MODELS ---------------- */

enum class PaymentStatus { PAID, UNPAID }

data class Lesson(
    val subject: String,
    val grade: String,
    val student: String,
    val time: String,
    val paymentStatus: PaymentStatus
)

data class LessonsFilter(
    val paymentStatus: PaymentStatus? = null,
    val subject: String? = null,
    val grade: String? = null
)

/* ---------------- SCREEN ---------------- */

@Composable
fun LessonsListScreen() {

    val background = Color(0xFF020617)

    val allLessons = remember {
        listOf(
            Lesson("Английский язык", "7 класс", "Светлана Ерохина", "15:00 – 16:00", PaymentStatus.UNPAID),
            Lesson("Подготовка к ОГЭ", "9 класс", "Иван Иванов", "17:00 – 18:00", PaymentStatus.PAID),
            Lesson("Математика", "6 класс", "Анна Петрова", "18:30 – 19:30", PaymentStatus.UNPAID)
        )
    }

    var filter by remember { mutableStateOf(LessonsFilter()) }
    var isFilterOpen by remember { mutableStateOf(false) }

    val filteredLessons by remember {
        derivedStateOf {
            allLessons.filter {
                (filter.paymentStatus == null || it.paymentStatus == filter.paymentStatus) &&
                        (filter.subject == null || it.subject == filter.subject) &&
                        (filter.grade == null || it.grade == filter.grade)
            }
        }
    }

    Surface(modifier = Modifier.fillMaxSize(), color = background) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(horizontal = 20.dp)
        ) {

            LessonsTopBar(
                onBackClick = {},
                onFilterClick = { isFilterOpen = true }
            )

            Spacer(modifier = Modifier.height(16.dp))

            LazyColumn(
                modifier = Modifier.weight(1f),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                items(filteredLessons) { lesson ->
                    LessonCard(lesson)
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            BottomNavPlaceholder()
        }

        if (isFilterOpen) {
            FilterSheet(
                currentFilter = filter,
                onApply = {
                    filter = it
                    isFilterOpen = false
                },
                onDismiss = { isFilterOpen = false }
            )
        }
    }
}

/* ---------------- TOP BAR ---------------- */

@Composable
private fun LessonsTopBar(
    onBackClick: () -> Unit,
    onFilterClick: () -> Unit
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 16.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {

        Box(
            modifier = Modifier
                .size(40.dp)
                .border(2.dp, Color(0xFF334155), RoundedCornerShape(12.dp))
                .clickable { onBackClick() }
        )

        Spacer(modifier = Modifier.weight(1f))

        Text(
            text = "Список занятий",
            color = Color.White,
            fontSize = 22.sp,
            fontWeight = FontWeight.SemiBold
        )

        Spacer(modifier = Modifier.weight(1f))

        Box(
            modifier = Modifier
                .size(40.dp)
                .border(2.dp, Color(0xFF334155), RoundedCornerShape(12.dp))
                .clickable { onFilterClick() }
        )
    }
}

/* ---------------- CARD ---------------- */

@Composable
private fun LessonCard(lesson: Lesson) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .border(3.dp, Color(0xFF334155), RoundedCornerShape(20.dp))
            .padding(16.dp)
    ) {

        PaymentStatusBadge(lesson.paymentStatus)

        Spacer(modifier = Modifier.height(10.dp))

        Text(
            text = "${lesson.subject} • ${lesson.grade}",
            color = Color.White,
            fontSize = 16.sp,
            fontWeight = FontWeight.Medium
        )

        Spacer(modifier = Modifier.height(6.dp))

        Text(
            text = lesson.student,
            color = Color(0xFFCBD5E1),
            fontSize = 14.sp
        )

        Spacer(modifier = Modifier.height(10.dp))

        Text(
            text = lesson.time,
            color = Color(0xFF075985),
            fontSize = 14.sp,
            fontWeight = FontWeight.Medium
        )
    }
}

/* ---------------- PAYMENT BADGE ---------------- */

@Composable
private fun PaymentStatusBadge(status: PaymentStatus) {

    val (text, color) = when (status) {
        PaymentStatus.PAID -> "Оплачено" to Color(0xFF16A34A)
        PaymentStatus.UNPAID -> "Не оплачено" to Color(0xFFDC2626)
    }

    Box(
        modifier = Modifier
            .border(1.dp, color, RoundedCornerShape(12.dp))
            .padding(horizontal = 10.dp, vertical = 4.dp)
    ) {
        Text(text, color = color, fontSize = 12.sp)
    }
}

/* ---------------- FILTER SHEET ---------------- */

@Composable
private fun FilterSheet(
    currentFilter: LessonsFilter,
    onApply: (LessonsFilter) -> Unit,
    onDismiss: () -> Unit
) {
    Box(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        contentAlignment = Alignment.BottomCenter
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .border(3.dp, Color(0xFF334155), RoundedCornerShape(20.dp))
                .padding(16.dp)
        ) {

            Text("Фильтрация", color = Color.White, fontSize = 18.sp)

            Spacer(modifier = Modifier.height(12.dp))

            FilterOption("Только оплаченные") {
                onApply(currentFilter.copy(paymentStatus = PaymentStatus.PAID))
            }

            FilterOption("Только неоплаченные") {
                onApply(currentFilter.copy(paymentStatus = PaymentStatus.UNPAID))
            }

            FilterOption("Сбросить фильтры") {
                onApply(LessonsFilter())
            }
        }
    }
}

@Composable
private fun FilterOption(text: String, onClick: () -> Unit) {
    Text(
        text = text,
        color = Color(0xFF38BDF8),
        fontSize = 14.sp,
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 8.dp)
            .clickable { onClick() }
    )
}

/* ---------------- BOTTOM NAV ---------------- */

@Composable
private fun BottomNavPlaceholder() {
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .height(72.dp)
            .border(3.dp, Color(0xFF134E4A), RoundedCornerShape(30.dp))
    )
}
