package com.example.tutorhammer

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.navigation.compose.rememberNavController
import com.example.tutorhammer.ui.navigation.AppNavGraph

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {

            // создаём контроллер навигации
            val navController = rememberNavController()

            // общий фон приложения
            Surface(
                modifier = Modifier,
                color = Color(0xFF171717)
            ) {
                // запускаем навигацию
                AppNavGraph(navController)
            }
        }
    }
}
