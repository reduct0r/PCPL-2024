package part_2

import kotlin.reflect.KClass
import kotlin.reflect.full.memberFunctions
import kotlin.reflect.full.memberProperties


fun printReflectionInfo(kClass: KClass<*>) {
    println("Constructors:")
    for (constructor in kClass.constructors) {
        println(constructor)
    }

    println("\nProperties:")
    for (property in kClass.memberProperties) {
        println("${property.name}: ${property.returnType}")
    }

    println("\nMethods:")
    for (function in kClass.memberFunctions) {
        println("${function.name}(${function.parameters.joinToString(", ") { it.name ?: "param" }})")
    }
}

fun callMethodUsingReflection(instance: Any, methodName: String, vararg args: Any?) {
    val kClass = instance::class
    val method = kClass.memberFunctions.find { it.name == methodName }
    if (method != null) {
        val result = method.call(instance, *args)
        println("Result of $methodName: $result")
    } else {
        println("Method $methodName not found.")
    }
}

fun main() {
    println("=======Printing reflection info =======")
    printReflectionInfo(Person::class) // Person::class is a KClass instance
    println("\n")

    println("=======Printing annotated properties =======")
    printAnnotatedProperties(Person::class)
    println("\n")

    println("=======Calling method using reflection ======='")
    val person = Person("Alice", 30)
    callMethodUsingReflection(person, "greet", "Hello")
    println("\n")

    println("=======Calling method using reflection with wrong method name =======")
    callMethodUsingReflection(person, "badMethod", "Hello")
    println("\n")
}