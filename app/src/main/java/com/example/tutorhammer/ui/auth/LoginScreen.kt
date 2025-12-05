package com.example.tutorhammer.ui.auth

import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.text.style.TextDecoration
import androidx.navigation.NavHostController
import com.example.tutorhammer.ui.navigation.Screen


@Composable
fun LoginScreen(navController: NavHostController) {


        // 🌟 Колонка, которая задаёт ОТСТУПЫ сверху/снизу
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(
                    horizontal = 32.dp,
                    vertical = 64.dp  // ← ВОТ ОНИ, ВСЁ УПРАВЛЕНИЕ ВЫСОТОЙ
                ),
            verticalArrangement = Arrangement.Center, // ← центрирование карточки
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            // 🌟 САМА КАРТОЧКА — высоту мы НЕ задаём ВООБЩЕ
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .border(
                        width = 3.dp,
                        color = Color(0xFF334155),
                        shape = RoundedCornerShape(28.dp)
                    )
                    .padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {

                // ----------------------------
                // Заголовок "Вход"
                // ----------------------------
                Text(
                    text = "Вход",
                    fontSize = 18.sp,
                    fontWeight = FontWeight.Black,
                    color = Color(0xFFF8FAFC)
                )

                Spacer(modifier = Modifier.height(24.dp))

                // ----------------------------
                // Поле "Номер телефона"
                // ----------------------------
                var phone by remember { mutableStateOf("") }

                Text(
                    text = "Номер телефона",
                    fontSize = 12.sp,
                    color = Color(0xFFF8FAFC),
                    modifier = Modifier
                        .align(Alignment.Start)
                        .padding(start = 8.dp)
                )

                Spacer(modifier = Modifier.height(6.dp))

                OutlinedTextField(
                    value = phone,
                    onValueChange = { phone = it },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(46.dp),
                    shape = RoundedCornerShape(24.dp),

                    colors = TextFieldDefaults.colors(
                        unfocusedContainerColor = Color.Transparent,
                        focusedContainerColor = Color.Transparent,
                        unfocusedIndicatorColor = Color(0xFF334155),
                        focusedIndicatorColor = Color(0xFF334155),
                        cursorColor = Color(0xFFF8FAFC),
                        focusedTextColor = Color(0xFFF8FAFC),
                        unfocusedTextColor = Color(0xFFF8FAFC)
                    )
                )

                Spacer(modifier = Modifier.height(16.dp))

                // ----------------------------
                // Поле "Пароль"
                // ----------------------------
                var password by remember { mutableStateOf("") }

                Text(
                    text = "Пароль",
                    fontSize = 12.sp,
                    color = Color(0xFFF8FAFC),
                    modifier = Modifier
                        .align(Alignment.Start)
                        .padding(start = 8.dp)

                )

                Spacer(modifier = Modifier.height(6.dp))

                OutlinedTextField(
                    value = password,
                    onValueChange = { password = it },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(46.dp),
                    shape = RoundedCornerShape(24.dp),

                    colors = TextFieldDefaults.colors(
                        unfocusedContainerColor = Color.Transparent,
                        focusedContainerColor = Color.Transparent,
                        unfocusedIndicatorColor = Color(0xFF334155),
                        focusedIndicatorColor = Color(0xFF334155),
                        cursorColor = Color(0xFFF8FAFC),
                        focusedTextColor = Color(0xFFF8FAFC),
                        unfocusedTextColor = Color(0xFFF8FAFC)
                    )
                )


                Spacer(modifier = Modifier.height(24.dp))

                // ----------------------------
                // Кнопка "Проходите"
                // ----------------------------
                Button(
                    onClick = { },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(46.dp),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = Color(0xFF0F766E)
                    ),
                    shape = RoundedCornerShape(24.dp)
                ) {
                    Text("Проходите", color = Color.White)
                }

                Spacer(modifier = Modifier.height(24.dp))

                // ----------------------------
                // "Забыли пароль?"
                // ----------------------------
                Text(
                    text = "Забыли пароль?",
                    fontSize = 10.sp,
                    color = Color(0xFF94A3B8),
                    textDecoration = TextDecoration.Underline,
                    modifier = Modifier.clickable { }
                )

                Spacer(modifier = Modifier.height(24.dp))

                // ----------------------------
                // "Нет аккаунта? Тогда регистрируйся"
                // ----------------------------
                Row {
                    Text(
                        text = "Нет аккаунта? Тогда ",
                        fontSize = 12.sp,
                        color = Color(0xFFF8FAFC)
                    )

                    Text(
                        text = "регистрируйся",
                        fontSize = 12.sp,
                        color = Color(0xFF0F766E),
                        textDecoration = TextDecoration.Underline,
                        modifier = Modifier.clickable {
                            navController.navigate(Screen.Registration.route)
                        }
                    )
                }
            }
        }
    }

