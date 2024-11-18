package part_2

import kotlin.reflect.KClass
import kotlin.reflect.full.findAnnotation
import kotlin.reflect.full.memberProperties

class Person {
    @Important("The person's name")
    private var name: String

    private var age: Int

    // Первичный конструктор
    constructor(){
        println("First constructor")
        name = "Unknown"
        age = 0
    }

    // Init блок
    init {
        println("Init block")
        name = "Unknown"
        age = 0
    }

    // Конструктор с параметрами
    constructor(name: String, age: Int) {
        this.name = name
        this.age = age
    }

    // Метод, который возвращает информацию о человеке
    fun getInfo(): String {
        return "Name: $name, Age: $age"
    }

    // Метод с параметром
    fun greet(greeting: String): String {
        return "$greeting, my name is $name."
    }
}

// Функция для вывода информации о классе
fun printAnnotatedProperties(kClass: KClass<*>) {
    println("Annotated Properties:")
    for (property in kClass.memberProperties) {
        val annotation = property.findAnnotation<Important>()
        if (annotation != null) {
            println("${property.name}: ${annotation.description}")
        }
    }
}
