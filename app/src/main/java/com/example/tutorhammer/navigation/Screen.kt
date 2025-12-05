package com.example.tutorhammer.ui.navigation

sealed class Screen(val route: String) {
    data object Login : Screen("login")
    data object Registration : Screen("registration")
}

// todo: надо отрисовать старт скрин