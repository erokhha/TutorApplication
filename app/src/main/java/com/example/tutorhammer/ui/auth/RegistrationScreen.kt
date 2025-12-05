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


@Composable
fun RegistrationScreen(navController: NavHostController) {


        // 🌟 Задаём расстояние до границ экрана через паддинги
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(horizontal = 32.dp, vertical = 80.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            // 🌟 Карточка регистрации — БЕЗ фиксированных размеров
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
                // Заголовок «Регистрация»
                // ----------------------------
                Text(
                    text = "Регистрация",
                    fontSize = 18.sp,
                    fontWeight = FontWeight.Black,
                    color = Color(0xFFF8FAFC)
                )

                Spacer(modifier = Modifier.height(24.dp))

                //----------------------------------
                // Поле «Номер телефона»
                //----------------------------------
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
                        unfocusedTextColor = Color(0xFFF8FAFC),
                        focusedTextColor = Color(0xFFF8FAFC)
                    )
                )

                Spacer(modifier = Modifier.height(16.dp))

                //----------------------------------
                // Поле «Почта»
                //----------------------------------
                var email by remember { mutableStateOf("") }

                Text(
                    text = "Почта",
                    fontSize = 12.sp,
                    color = Color(0xFFF8FAFC),
                    modifier = Modifier
                        .align(Alignment.Start)
                        .padding(start = 8.dp)
                )

                Spacer(modifier = Modifier.height(6.dp))

                OutlinedTextField(
                    value = email,
                    onValueChange = { email = it },
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
                        unfocusedTextColor = Color(0xFFF8FAFC),
                        focusedTextColor = Color(0xFFF8FAFC)
                    )
                )

                Spacer(modifier = Modifier.height(16.dp))

                //----------------------------------
                // Поле «Пароль»
                //----------------------------------
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
                        unfocusedTextColor = Color(0xFFF8FAFC),
                        focusedTextColor = Color(0xFFF8FAFC)
                    )
                )

                Spacer(modifier = Modifier.height(16.dp))

                //----------------------------------
                // Поле «Повторить пароль»
                //----------------------------------
                var passwordRepeat by remember { mutableStateOf("") }

                Text(
                    text = "Повторить пароль",
                    fontSize = 12.sp,
                    color = Color(0xFFF8FAFC),
                    modifier = Modifier
                        .align(Alignment.Start)
                        .padding(start = 8.dp)
                )

                Spacer(modifier = Modifier.height(6.dp))

                OutlinedTextField(
                    value = passwordRepeat,
                    onValueChange = { passwordRepeat = it },
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
                        unfocusedTextColor = Color(0xFFF8FAFC),
                        focusedTextColor = Color(0xFFF8FAFC)
                    )
                )

                Spacer(modifier = Modifier.height(24.dp))

                //----------------------------------
                // Кнопки «Я ученик» / «Я репетитор»
                //----------------------------------
                Row(
                    horizontalArrangement = Arrangement.SpaceEvenly,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Text(
                        text = "Я ученик",
                        color = Color(0xFF0F766E),
                        fontSize = 12.sp,
                        textDecoration = TextDecoration.Underline,
                        modifier = Modifier.clickable { }
                    )
                    Text(
                        text = "Я репетитор",
                        color = Color(0xFF0F766E),
                        fontSize = 12.sp,
                        textDecoration = TextDecoration.Underline,
                        modifier = Modifier.clickable { }
                    )
                }
                Spacer(modifier = Modifier.height(24.dp))

                Text(
                    text = "Назад ко входу",
                    color = Color(0xFF94A3B8),        // светло-серый
                    fontSize = 12.sp,
                    modifier = Modifier.clickable {
                        navController.popBackStack()
                    }
                )

            }
        }
    }

