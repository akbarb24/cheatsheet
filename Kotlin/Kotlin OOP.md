_Based on material By Eko Kurniawan Khannedy_

---

## 📋 Content List

1. [[#Class & Object]]
2. [[#Properties]]
3. [[#Constructor]]
4. [[#Function]]
5. [[#This Keyword]]
6. [[#Inheritance]]
7. [[#Function Overriding]]
8. [[#Properties Overriding]]
9. [[#Super Keyword]]
10. [[#Any Class]]
11. [[#Type Check & Casts]]
12. [[#toString Function]]
13. [[#Equals Function]]
14. [[#HashCode Function]]
15. [[#Abstract Class]]
16. [[#Getter and Setter]]
17. [[#Late-Initialized Properties]]
18. [[#Interface]]
19. [[#Visibility Modifiers]]
20. [[#Extension Function]]
21. [[#Extension Properties]]
22. [[#Data Class]]
23. [[#Sealed Class]]
24. [[#Inner Class]]
25. [[#Anonymous Class]]
26. [[#Enum Class]]
27. [[#Singleton Object]]
28. [[#Companion Object]]
29. [[#Type Alias]]
30. [[#Inline Class]]
31. [[#Delegation]]
32. [[#Lazy Properties]]
33. [[#Observable Properties]]
34. [[#Destructuring Declarations]]
35. [[#Operator Overloading]]
36. [[#Null Safety]]
37. [[#Exception]]
38. [[#Annotation]]
39. [[#Reflection]]
40. [[#Scope Functions]]
41. [[#Polymorphism]]

---

## Class & Object

[[#📋 Content List|↑ Back to Content]]

**Blueprint and instances for creating objects in Kotlin**

### Creating a Class

```kotlin
class Person

class Car

class Customer
```

### Creating an Object

```kotlin
val person = Person()
val car = Car()
val customer = Customer()
```

**Note:** No `new` keyword needed in Kotlin!

---

## Properties

[[#📋 Content List|↑ Back to Content]]

**Data fields/attributes that objects can hold**

### Declaring Properties

```kotlin
class Person {
    var firstName: String = ""
    var lastName: String = ""
    val age: Int = 0
}
```

### Manipulating Properties

```kotlin
val person = Person()
person.firstName = "John"
person.lastName = "Doe"
println(person.firstName) // John
```

---

## Constructor

[[#📋 Content List|↑ Back to Content]]

**Special functions to initialize objects when created**

### Primary Constructor

```kotlin
class Person(firstName: String, lastName: String) {
    val firstName: String = firstName
    val lastName: String = lastName
}

val person = Person("John", "Doe")
```

### Initializer Block

```kotlin
class Person(name: String) {
    init {
        println("Person $name created")
    }
}
```

### Secondary Constructor

```kotlin
class Person(val firstName: String, val lastName: String) {
    constructor(name: String) : this(name, "")
}
```

### Properties in Constructor

```kotlin
class Person(
    val firstName: String,
    val lastName: String,
    val age: Int
)
```

---

## Function

[[#📋 Content List|↑ Back to Content]]

**Behaviors/methods that objects can perform**

### Declaring Functions

```kotlin
class Person(val name: String) {
    fun sayHello(otherName: String) {
        println("Hello $otherName, my name is $name")
    }
}
```

### Function Overloading

```kotlin
class Calculator {
    fun add(a: Int, b: Int): Int = a + b
    fun add(a: Double, b: Double): Double = a + b
    fun add(a: Int, b: Int, c: Int): Int = a + b + c
}
```

---

## This Keyword

[[#📋 Content List|↑ Back to Content]]

**Reference to the current object instance**

```kotlin
class Person(name: String) {
    val name: String
    
    init {
        this.name = name // this refers to current object
    }
}
```

---

## Inheritance

[[#📋 Content List|↑ Back to Content]]

**Mechanism to create child classes from parent classes**

### Basic Inheritance

```kotlin
open class Employee(val name: String)

class Manager(name: String) : Employee(name)

class VicePresident(name: String) : Employee(name)
```

**Note:** Use `open` keyword to make class inheritable!

---

## Function Overriding

[[#📋 Content List|↑ Back to Content]]

**Redefining parent class functions in child classes**

```kotlin
open class Employee(val name: String) {
    open fun sayHello(name: String) {
        println("Hello $name, my name is ${this.name}")
    }
}

class Manager(name: String) : Employee(name) {
    override fun sayHello(name: String) {
        println("Hello $name, I'm Manager ${this.name}")
    }
}
```

### Final Override Function

```kotlin
open class Employee {
    open fun work() { }
}

open class Manager : Employee() {
    final override fun work() { } // Cannot be overridden anymore
}
```

---

## Properties Overriding

[[#📋 Content List|↑ Back to Content]]

**Redefining parent class properties in child classes**

```kotlin
open class Shape {
    open val corner: Int = 0
}

class Rectangle : Shape() {
    override val corner: Int = 4
}
```

---

## Super Keyword

[[#📋 Content List|↑ Back to Content]]

**Access parent class members from child class**

### Accessing Parent Properties

```kotlin
open class Shape {
    open val corner: Int = 0
}

class Rectangle : Shape() {
    override val corner: Int = 4
    val parentCorner = super.corner
}
```

### Accessing Parent Functions

```kotlin
open class Employee {
    open fun sayHello() {
        println("Hello from Employee")
    }
}

class Manager : Employee() {
    override fun sayHello() {
        super.sayHello()
        println("Hello from Manager")
    }
}
```

### Super Constructor

```kotlin
open class Employee(name: String)

class Manager(name: String) : Employee(name)
```

---

## Any Class

[[#📋 Content List|↑ Back to Content]]

**The root superclass of all Kotlin classes**

All classes in Kotlin inherit from `Any` by default.

**Any class has 3 methods:**

- `equals()`: Object comparison
- `hashCode()`: Numeric representation
- `toString()`: String representation

---

## Type Check & Casts

[[#📋 Content List|↑ Back to Content]]

**Checking and converting object types at runtime**

### is and !is Operator

```kotlin
fun printObject(any: Any) {
    if (any is String) {
        println("String: $any")
    } else if (any is Int) {
        println("Int: $any")
    } else {
        println("Unknown")
    }
}
```

### Smart Casts

```kotlin
if (any is String) {
    println(any.toUpperCase()) // Automatically casted to String
}
```

### When Expression

```kotlin
when (any) {
    is String -> println(any.toUpperCase())
    is Int -> println(any * 10)
    else -> println("Unknown")
}
```

### Unsafe Casts

```kotlin
val string: String = any as String // Throws exception if fails
```

### Safe Nullable Casts

```kotlin
val string: String? = any as? String // Returns null if fails
```

---

## toString Function

[[#📋 Content List|↑ Back to Content]]

**String representation of an object**

```kotlin
class Product(val name: String, val price: Int) {
    override fun toString(): String {
        return "Product(name='$name', price=$price)"
    }
}
```

---

## Equals Function

[[#📋 Content List|↑ Back to Content]]

**Custom object comparison logic**

```kotlin
class Product(val name: String, val price: Int) {
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Product) return false
        
        if (name != other.name) return false
        if (price != other.price) return false
        
        return true
    }
}
```

---

## HashCode Function

[[#📋 Content List|↑ Back to Content]]

**Numeric representation for object identification**

```kotlin
class Product(val name: String, val price: Int) {
    override fun hashCode(): Int {
        var result = name.hashCode()
        result = 31 * result + price
        return result
    }
}
```

---

## Abstract Class

[[#📋 Content List|↑ Back to Content]]

**Classes that cannot be instantiated, only inherited**

### Basic Abstract Class

```kotlin
abstract class Location(val name: String)

class City(name: String) : Location(name)
class Country(name: String) : Location(name)
```

### Abstract Properties & Function

```kotlin
abstract class Animal {
    abstract val name: String
    abstract fun run()
}

class Cat : Animal() {
    override val name: String = "Cat"
    override fun run() {
        println("Cat is running")
    }
}
```

---

## Getter and Setter

[[#📋 Content List|↑ Back to Content]]

**Custom accessors for properties**

```kotlin
class Person {
    var name: String = ""
        get() = field.toUpperCase()
        set(value) {
            field = value.trim()
        }
}

// Only Getter
class Person {
    val name: String = "Guest"
        get() = field.toUpperCase()
}
```

---

## Late-Initialized Properties

[[#📋 Content List|↑ Back to Content]]

**Properties initialized after object creation**

```kotlin
class Person {
    lateinit var name: String
    
    fun initName() {
        name = "John Doe"
    }
}

val person = Person()
person.initName()
println(person.name)
```

---

## Interface

[[#📋 Content List|↑ Back to Content]]

**Contracts defining what classes must implement**

### Basic Interface

```kotlin
interface Interaction {
    val name: String // abstract by default
    fun sayHello(name: String) // abstract by default
}

class Human(override val name: String) : Interaction {
    override fun sayHello(name: String) {
        println("Hello $name, my name is ${this.name}")
    }
}
```

### Concrete Function in Interface

```kotlin
interface Interaction {
    fun sayHello(name: String) {
        println("Hello $name")
    }
}
```

### Multiple Inheritance

```kotlin
interface Go {
    fun go() = println("Go!")
}

interface Stop {
    fun stop() = println("Stop!")
}

class Car : Go, Stop
```

### Interface Inheritance

```kotlin
interface Base {
    fun base()
}

interface Child : Base {
    fun child()
}
```

---

## Visibility Modifiers

[[#📋 Content List|↑ Back to Content]]

**Access control for classes, functions, and properties**

|Modifier|Description|
|---|---|
|`public`|Accessible from anywhere (default)|
|`private`|Only accessible in declaration place|
|`protected`|Accessible in declaration and child classes|
|`internal`|Accessible in same module/project|

```kotlin
open class Product {
    public val publicName: String = "Public"
    private val privateName: String = "Private"
    protected val protectedName: String = "Protected"
    internal val internalName: String = "Internal"
}
```

---

## Extension Function

[[#📋 Content List|↑ Back to Content]]

**Adding functions to existing types without inheritance**

```kotlin
fun String.hello(): String {
    return "Hello $this"
}

val result = "World".hello() // Hello World
```

### Nullable Extension Function

```kotlin
fun String?.helloSafe(): String {
    if (this == null) return "Hello Null"
    return "Hello $this"
}

val result: String? = null
println(result.helloSafe()) // Hello Null
```

---

## Extension Properties

[[#📋 Content List|↑ Back to Content]]

**Adding properties to existing types**

```kotlin
val String.firstChar: Char
    get() = this[0]

val name = "Kotlin"
println(name.firstChar) // K
```

---

## Data Class

[[#📋 Content List|↑ Back to Content]]

**Classes optimized for holding data with auto-generated methods**

```kotlin
data class Product(val name: String, val price: Int)

val product = Product("Laptop", 10000)
println(product) // Product(name=Laptop, price=10000)
```

### Copy Function

```kotlin
val product1 = Product("Laptop", 10000)
val product2 = product1.copy(price = 12000)
```

**Auto-generated functions:**

- `equals()`
- `hashCode()`
- `toString()`
- `copy()`
- `componentN()`

---

## Sealed Class

[[#📋 Content List|↑ Back to Content]]

**Restricted class hierarchies with limited subclasses**

```kotlin
sealed class Result

class Success(val data: String) : Result()
class Error(val message: String) : Result()
object Loading : Result()
```

### Sealed Class in When Expression

```kotlin
fun handleResult(result: Result) = when(result) {
    is Success -> println("Success: ${result.data}")
    is Error -> println("Error: ${result.message}")
    Loading -> println("Loading...")
}
```

---

## Inner Class

[[#📋 Content List|↑ Back to Content]]

**Classes nested inside other classes with access to outer class**

```kotlin
class House(val address: String) {
    inner class Room(val name: String) {
        fun getAddress(): String {
            return this@House.address
        }
    }
}

val house = House("Jakarta")
val room = house.Room("Bedroom")
println(room.getAddress()) // Jakarta
```

---

## Anonymous Class

[[#📋 Content List|↑ Back to Content]]

**Classes created without explicit declaration**

```kotlin
interface Action {
    fun action()
}

val action = object : Action {
    override fun action() {
        println("Action executed")
    }
}

action.action()
```

---

## Enum Class

[[#📋 Content List|↑ Back to Content]]

**Fixed set of constant values with type safety**

### Basic Enum

```kotlin
enum class Gender {
    MALE, FEMALE
}

val gender = Gender.MALE
```

### Enum with Properties & Functions

```kotlin
enum class Direction(val code: Int) {
    NORTH(0),
    SOUTH(180),
    EAST(90),
    WEST(270);
    
    fun getOpposite(): Direction = when(this) {
        NORTH -> SOUTH
        SOUTH -> NORTH
        EAST -> WEST
        WEST -> EAST
    }
}
```

---

## Singleton Object

[[#📋 Content List|↑ Back to Content]]

**Objects with only one instance throughout the app**

```kotlin
object Application {
    val name: String = "My Application"
    
    fun start() {
        println("Application started")
    }
}

Application.start()
println(Application.name)
```

### Inner Object

```kotlin
class Company {
    object Config {
        const val NAME = "My Company"
    }
}

println(Company.Config.NAME)
```

---

## Companion Object

[[#📋 Content List|↑ Back to Content]]

**Static-like members for classes in Kotlin**

```kotlin
class User {
    companion object {
        fun create(name: String): User {
            return User()
        }
    }
}

val user = User.create("John")
```

---

## Type Alias

[[#📋 Content List|↑ Back to Content]]

**Alternative names for existing types**

### For Class

```kotlin
typealias StringMap = Map<String, String>

val map: StringMap = mapOf("key" to "value")
```

### For Function

```kotlin
typealias Lambda = (String) -> String

fun process(name: String, lambda: Lambda): String {
    return lambda(name)
}
```

---

## Inline Class

[[#📋 Content List|↑ Back to Content]]

**Wrapper classes with zero runtime overhead**

```kotlin
@JvmInline
value class Token(val value: String)

val token = Token("abc123")
```

**Benefits:** No memory overhead, just compile-time type safety!

---

## Delegation

[[#📋 Content List|↑ Back to Content]]

**Forwarding implementation to another object**

```kotlin
interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() { println(x) }
}

class Derived(b: Base) : Base by b

val base = BaseImpl(10)
val derived = Derived(base)
derived.print() // 10
```

### Override Delegation

```kotlin
class Derived(b: Base) : Base by b {
    override fun print() { 
        println("Derived")
    }
}
```

---

## Lazy Properties

[[#📋 Content List|↑ Back to Content]]

**Properties initialized only when first accessed**

```kotlin
class Heavy {
    val data: String by lazy {
        println("Computing data...")
        "Heavy Data"
    }
}

val heavy = Heavy()
println(heavy.data) // Computing data... Heavy Data
println(heavy.data) // Heavy Data (no computation)
```

---

## Observable Properties

[[#📋 Content List|↑ Back to Content]]

**Properties that notify when values change**

```kotlin
import kotlin.properties.Delegates

class Person {
    var name: String by Delegates.observable("NoName") { 
        property, oldValue, newValue ->
        println("${property.name}: $oldValue -> $newValue")
    }
}

val person = Person()
person.name = "John" // name: NoName -> John
```

---

## Destructuring Declarations

[[#📋 Content List|↑ Back to Content]]

**Extracting multiple values from objects**

### With Data Class

```kotlin
data class User(val name: String, val age: Int)

val user = User("John", 30)
val (name, age) = user
println("$name is $age years old")
```

### In Function

```kotlin
fun getUser() = User("Alice", 25)

val (name, age) = getUser()
```

### Underscore for Unused Variables

```kotlin
val (name, _) = user // Ignore age
```

### In Lambda

```kotlin
val users = listOf(User("John", 30), User("Jane", 25))
users.forEach { (name, age) ->
    println("$name: $age")
}
```

---

## Operator Overloading

[[#📋 Content List|↑ Back to Content]]

*_Custom behavior for operators like +, -, _, etc.__

### Unary Operators

```kotlin
data class Point(val x: Int, val y: Int) {
    operator fun unaryMinus() = Point(-x, -y)
}

val point = Point(10, 20)
println(-point) // Point(x=-10, y=-20)
```

### Arithmetic Operators

```kotlin
data class Point(val x: Int, val y: Int) {
    operator fun plus(other: Point) = Point(x + other.x, y + other.y)
}

val p1 = Point(10, 20)
val p2 = Point(5, 10)
println(p1 + p2) // Point(x=15, y=30)
```

### Comparison Operators

```kotlin
class Version(val major: Int, val minor: Int) {
    operator fun compareTo(other: Version): Int {
        if (major != other.major) return major - other.major
        return minor - other.minor
    }
}

val v1 = Version(1, 0)
val v2 = Version(2, 0)
println(v1 < v2) // true
```

### Invoke Operator

```kotlin
class Greeter(val greeting: String) {
    operator fun invoke(name: String) {
        println("$greeting, $name!")
    }
}

val greeter = Greeter("Hello")
greeter("World") // Hello, World!
```

---

## Null Safety

[[#📋 Content List|↑ Back to Content]]

**Preventing null pointer exceptions**

### Checking for Null

```kotlin
val name: String? = null
if (name != null) {
    println(name.length)
}
```

### Safe Call (?.)

```kotlin
val length = name?.length // Returns null if name is null
```

### Elvis Operator (?:)

```kotlin
val length = name?.length ?: 0 // Returns 0 if name is null
```

### Not-Null Assertion (!!)

```kotlin
val length = name!!.length // Throws exception if name is null
```

---

## Exception

[[#📋 Content List|↑ Back to Content]]

**Error handling and throwing exceptions**

### Throwing Exception

```kotlin
fun divide(a: Int, b: Int): Int {
    if (b == 0) {
        throw IllegalArgumentException("Cannot divide by zero")
    }
    return a / b
}
```

### Try Catch

```kotlin
try {
    val result = divide(10, 0)
    println(result)
} catch (e: IllegalArgumentException) {
    println("Error: ${e.message}")
}
```

### Multiple Catch

```kotlin
try {
    // code
} catch (e: IllegalArgumentException) {
    println("Illegal Argument")
} catch (e: Exception) {
    println("General Exception")
}
```

### Finally

```kotlin
try {
    // code
} catch (e: Exception) {
    println("Error")
} finally {
    println("Always executed")
}
```

---

## Annotation

[[#📋 Content List|↑ Back to Content]]

**Metadata attached to code elements**

### Creating Annotation

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.RUNTIME)
@MustBeDocumented
annotation class Fancy(val author: String)
```

### Using Annotation

```kotlin
@Fancy(author = "John Doe")
class MyClass
```

### Annotation Target

```kotlin
class Person {
    @get:Fancy(author = "John")
    val name: String = "John"
}
```

---

## Reflection

[[#📋 Content List|↑ Back to Content]]

**Inspecting code structure at runtime**

```kotlin
val person = Person()
val kClass = person::class

println(kClass.simpleName) // Person
println(kClass.qualifiedName) // com.example.Person

// Or from class directly
val kClass2 = Person::class
```

---

## Scope Functions

[[#📋 Content List|↑ Back to Content]]

**Functions for executing code blocks on objects (let, run, apply, also, with)**

### let

```kotlin
val name: String? = "Kotlin"
name?.let {
    println(it.toUpperCase())
}
```

### run

```kotlin
val result = "Kotlin".run {
    println(this.toUpperCase())
    length
}
```

### apply

```kotlin
val person = Person().apply {
    firstName = "John"
    lastName = "Doe"
}
```

### also

```kotlin
val numbers = mutableListOf(1, 2, 3).also {
    println("Initial list: $it")
}.add(4)
```

### with

```kotlin
val result = with("Kotlin") {
    println(this.toUpperCase())
    length
}
```

### Summary

|Function|Object Reference|Return Value|Use Case|
|---|---|---|---|
|`let`|`it`|Lambda result|Null checks, transformations|
|`run`|`this`|Lambda result|Object configuration + computation|
|`apply`|`this`|Object itself|Object configuration|
|`also`|`it`|Object itself|Additional operations|
|`with`|`this`|Lambda result|Grouping function calls|

---

## Polymorphism

[[#📋 Content List|↑ Back to Content]]

**Objects taking multiple forms through inheritance**

```kotlin
open class Employee(val name: String) {
    open fun sayHello(name: String) {
        println("Hello $name, I'm employee ${this.name}")
    }
}

class Manager(name: String) : Employee(name) {
    override fun sayHello(name: String) {
        println("Hello $name, I'm manager ${this.name}")
    }
}

class VicePresident(name: String) : Employee(name) {
    override fun sayHello(name: String) {
        println("Hello $name, I'm VP ${this.name}")
    }
}

fun greet(employee: Employee) {
    employee.sayHello("World") // Polymorphic behavior
}

greet(Employee("John"))      // Hello World, I'm employee John
greet(Manager("Jane"))       // Hello World, I'm manager Jane
greet(VicePresident("Bob"))  // Hello World, I'm VP Bob
```

---

## 📚 Additional Resources

- **Next Topics:**
    
    - Kotlin Generic
    - Kotlin Collection
    - Kotlin Coroutine
- **Contact:**
    
    - YouTube: [Programmer Zaman Now](https://youtube.com/c/ProgrammerZamanNow)
    - Email: echo.khannedy@gmail.com

---

[[#📋 Content List|↑ Back to Content]]

_Created from Kotlin Object Oriented Programming by Eko Kurniawan Khannedy_