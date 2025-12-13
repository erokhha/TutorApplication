package com.example.tutorhammer.ui.navigation

sealed class Screen(val route: String) {
    data object Login : Screen("login")
    data object Registration : Screen("registration")
}

// ggfgf

// todo: надо отрисовать старт скрин