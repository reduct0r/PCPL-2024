package part_2

// Определение аннотации
@Target(AnnotationTarget.PROPERTY)                  // Аннотация применима к свойствам
@Retention(AnnotationRetention.RUNTIME)             // Аннотация будет доступна во время выполнения программы
annotation class Important(val description: String) // Аннотация с параметром description