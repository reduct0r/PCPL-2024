package part_1

// Определение типа функции (Аналог делегата)
typealias MyDelegate = (Int, String, Double) -> Any

// Метод аналогичный типу MyDelegate
fun sampleMethod(a: Int, b: String, c: Double): String {
    return "Int: $a, String: $b, Double: $c"
}

// Метод, который принимает делегат и вызывает его
fun executeDelegate(delegate: MyDelegate, a: Int, b: String, c: Double) {
    val result = delegate(a, b, c)
    println("Delegate result: $result")
}

// Обобщенный метод, который принимает делегат и вызывает его
fun executeGenericDelegate(delegate: (Int, String, Double) -> Any, a: Int, b: String, c: Double) {
    val result = delegate(a, b, c)
    println("Generic delegate result: $result")
}


fun main() {
    // Вызов с использованием метода sampleMethod
    executeDelegate(::sampleMethod, 10, "Hello", 20.5)

    // Вызов с использованием лямбда-выражения
    executeDelegate({ a, b, c -> "Lambda: $a, $b, $c" }, 30, "Kotlin", 40.5)

    // Вызов обобщенного метода с использованием sampleMethod
    executeGenericDelegate(::sampleMethod, 10, "Hello", 20.5)

    // Вызов обобщенного метода с использованием лямбда-выражения
    executeGenericDelegate({ a, b, c -> "Lambda: $a, $b, $c" }, 30, "Kotlin", 40.5)
}
