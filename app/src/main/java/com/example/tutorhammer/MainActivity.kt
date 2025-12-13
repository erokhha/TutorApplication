package com.example.tutorhammer
import com.example.tutorhammer.ui.tutor.lessons.LessonsListScreen


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
            Surface(
                modifier = Modifier,
                color = Color(0xFF171717)
            ) {
                // Показываем твоё окно без навигации
                LessonsListScreen()
            }
        }

    }
}

