package com.example.tutorhammer.ui.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.NavHostController
import com.example.tutorhammer.ui.auth.LoginScreen
import com.example.tutorhammer.ui.auth.RegistrationScreen

@Composable
fun AppNavGraph(navController: NavHostController) {
    NavHost(
        navController = navController,
        startDestination = Screen.Login.route
    ) {
        composable(Screen.Login.route) {
            LoginScreen(navController)
        }
        composable(Screen.Registration.route) {
            RegistrationScreen(navController)
        }
    }
}
