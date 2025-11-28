**Author:** Eko Kurniawan Khannedy  
**Source:** Programmer Zaman Now

---

## 📋 Content List

1. [Introduction to Generic](#introduction-to-generic)
2. [Generic Class](#generic-class)
3. [Generic Function](#generic-function)
4. [Invariant](#invariant)
5. [Covariant](#covariant)
6. [Contravariant](#contravariant)
7. [Generic Constraints](#generic-constraints)
8. [Type Projection](#type-projection)
9. [Star Projection](#star-projection)
10. [Type Erasure](#type-erasure)
11. [Comparable Interface](#comparable-interface)
12. [Delegate Interfaces](#delegate-interfaces)
    - [ReadOnlyProperty Interface](#readonlyproperty-interface)
    - [ReadWriteProperty Interface](#readwriteproperty-interface)
    - [ObservableProperty Class](#observableproperty-class)
13. [Generic Extension Function](#generic-extension-function)

---

## Introduction to Generic

Generics enable you to add type parameters when creating classes or functions, allowing for flexible and reusable code that works with different data types.

**Key Benefits:**

- **Compile-time type checking** - Errors caught early
- **No manual type casting** - Type safety guaranteed
- **Code reusability** - Write once, use with multiple types

**Common Generic Parameter Names:**

- `E` - Element (collections/data structures)
- `K` - Key
- `N` - Number
- `T` - Type
- `V` - Value
- `S, U, V` - 2nd, 3rd, 4th types

**Example:**

```kotlin
// Without Generic
class Container(val data: Any)

// With Generic
class Container<T>(val data: T)
```

[← Back to Contents](#content-list)

---

## Generic Class

A generic class or interface has type parameters that can be specified when creating instances.

**Single Parameter Type:**

```kotlin
class Box<T>(val content: T)

val stringBox = Box<String>("Hello")
val intBox = Box<Int>(123)
val numberBox = Box(42) // Type inference
```

**Multiple Parameter Types:**

```kotlin
class Pair<K, V>(val key: K, val value: V)

val pair = Pair<String, Int>("Age", 25)
```

**Key Points:**

- Type parameter can be any valid identifier
- Multiple type parameters must have different names
- Useful for creating flexible, reusable data structures

**Use Cases:**

- Collections (List<T>, Set<T>, Map<K,V>)
- Data containers
- Type-safe APIs

[← Back to Contents](#content-list)

---

## Generic Function

Generic type parameters can be applied to functions, not just classes.

**Syntax:**

```kotlin
fun <T> functionName(param: T): T {
    // function body
}
```

**Examples:**

```kotlin
// Single parameter
fun <T> printItem(item: T) {
    println(item)
}

// Multiple parameters
fun <T, U> combine(first: T, second: U): Pair<T, U> {
    return Pair(first, second)
}
```

**Key Points:**

- Type parameter declared before function name
- Type parameter scoped to function only
- Enables generic behavior without modifying class
- Type inference works automatically

**Usage:**

```kotlin
printItem(123)          // T = Int
printItem("Hello")      // T = String
combine("A", 1)         // T = String, U = Int
```

[← Back to Contents](#content-list)

---

## Invariant

By default, generic type parameters are invariant, meaning no substitution with subtypes or supertypes is allowed.

**Concept:**

- `Container<String>` ≠ `Container<Any>`
- `Container<Any>` ≠ `Container<String>`
- No type substitution allowed in either direction

**Example:**

```kotlin
class Container<T>(val data: T)

val stringContainer: Container<String> = Container("Hello")
// val anyContainer: Container<Any> = stringContainer // ERROR!
// val stringContainer2: Container<String> = Container<Any>("Hi") // ERROR!
```

**Why Invariant?**

- Safety: Prevents type confusion
- Both read and write operations are type-safe
- Default behavior for mutable data structures

**Key Point:** If a class both produces (returns) and consumes (accepts) type T, it should remain invariant.

[← Back to Contents](#content-list)

---

## Covariant

Covariant allows substitution of a subtype with its supertype (child → parent).

**Declaration:** Use the `out` keyword to make a type parameter covariant.

```kotlin
class Producer<out T>(val data: T) {
    fun get(): T = data
    // fun set(value: T) {} // NOT ALLOWED - can't consume T
}
```

**Usage:**

```kotlin
val stringProducer: Producer<String> = Producer("Hello")
val anyProducer: Producer<Any> = stringProducer // OK!
```

**Rules:**

- Type parameter can only be used in **out** positions (return types)
- Cannot be used in **in** positions (parameters)
- Read-only operations only

**When to Use:**

- Producer/supplier classes that only return values
- Immutable collections
- When class acts as a source of data

**Example:** `List<out T>` in Kotlin is covariant because it's read-only.

[← Back to Contents](#content-list)

---

## Contravariant

Contravariant allows substitution of a supertype with its subtype (parent → child).

**Declaration:** Use the `in` keyword to make a type parameter contravariant.

```kotlin
class Consumer<in T> {
    fun accept(value: T) {
        println(value)
    }
    // fun get(): T {} // NOT ALLOWED - can't produce T
}
```

**Usage:**

```kotlin
val anyConsumer: Consumer<Any> = Consumer<Any>()
val stringConsumer: Consumer<String> = anyConsumer // OK!
```

**Rules:**

- Type parameter can only be used in **in** positions (parameters)
- Cannot be used in **out** positions (return types)
- Write-only operations only

**When to Use:**

- Consumer classes that only accept values
- Comparators
- When class acts as a sink for data

**Example:** `Comparable<in T>` is contravariant.

[← Back to Contents](#content-list)

---

## Generic Constraints

Constrain generic type parameters to specific types or their subtypes.

**Single Constraint:**

```kotlin
// Only Number and its subtypes allowed
class NumberContainer<T : Number>(val value: T)

val intContainer = NumberContainer(123)     // OK
val doubleContainer = NumberContainer(3.14) // OK
// val stringContainer = NumberContainer("Hi") // ERROR!
```

**Multiple Constraints (where keyword):**

```kotlin
interface Printable {
    fun print()
}

class Document<T>(val content: T) where T : CharSequence, T : Printable

// T must implement both CharSequence AND Printable
```

**Default Constraint:**

- Without constraint, default is `Any?`
- All types are allowed

**Common Constraints:**

- `T : Number` - Numeric types only
- `T : Comparable<T>` - Comparable types
- `T : Any` - Non-nullable types only
- `T : SomeInterface` - Interface implementations

[← Back to Contents](#content-list)

---

## Type Projection

Use-site variance that allows specifying covariance or contravariance at the usage point, not declaration.

**Problem:** Sometimes a class is invariant by nature (has both input and output), but functions need flexibility.

**Solution: Type Projection**

**Out Projection (Covariant):**

```kotlin
fun copyFrom(source: Array<out Any>) {
    // Can read from source
    val item: Any = source[0] // OK
    // source[0] = "Hello" // ERROR - can't write
}
```

**In Projection (Contravariant):**

```kotlin
fun copyTo(dest: Array<in String>) {
    dest[0] = "Hello" // OK - can write
    // val item: String = dest[0] // ERROR - can't read as String
}
```

**When to Use:**

- Function parameters need variance but class is invariant
- Temporary flexibility without changing class declaration
- Working with arrays (which are invariant)

**Key Rules:**

- `out`: Read-only access (producer)
- `in`: Write-only access (consumer)

[← Back to Contents](#content-list)

---

## Star Projection

Use `*` when you don't care about the specific type parameter.

**Concept:** Sometimes you only need to work with the structure, not the specific type.

**Syntax:**

```kotlin
fun printArraySize(array: Array<*>) {
    println("Array size: ${array.size}")
    // Can't access elements in type-safe way
}
```

**Behavior:**

- `Array<*>` represents array of unknown type
- Can use members that don't involve type parameter
- Reading elements returns `Any?`
- Writing is not allowed (except null for nullable types)

**Examples:**

```kotlin
fun isListEmpty(list: List<*>): Boolean {
    return list.isEmpty() // OK - doesn't use type T
}

val anyList: List<*> = listOf(1, 2, 3)
val item: Any? = anyList[0] // OK - reads as Any?
```

**When to Use:**

- Only need to access type-independent members (size, isEmpty)
- Type parameter is irrelevant to operation
- Checking structure, not content

[← Back to Contents](#content-list)

---

## Type Erasure

Generic type information is checked at compile-time but erased at runtime.

**What Happens:**

1. Compiler checks generic types during compilation
2. Generic information removed from bytecode
3. Type parameters replaced with `Any` (or upper bound)

**Example:**

```kotlin
val stringList = listOf("a", "b")
val intList = listOf(1, 2)

// At runtime, both are just List
// Generic type information is gone
```

**Implications:**

```kotlin
// Can't check generic type at runtime
// if (obj is List<String>) {} // ERROR

// Can check raw type
if (obj is List<*>) {} // OK

// Can't get generic type via reflection
val list = listOf<String>("a", "b")
// list.javaClass.typeParameters returns empty at runtime
```

**Problems:**

```kotlin
fun <T> dangerous() {
    val list = mutableListOf<T>()
    // At runtime, could add wrong types!
}
```

**Why Type Erasure?**

- Java compatibility
- Runtime performance
- Backward compatibility with older code

**Best Practice:** Rely on compile-time checking, not runtime.

[← Back to Contents](#content-list)

---

## Comparable Interface

Enable comparison operations (>, <, >=, <=) by implementing `Comparable<T>`.

**Interface Definition:**

```kotlin
interface Comparable<in T> {
    operator fun compareTo(other: T): Int
}
```

**Return Values:**

- Negative: this < other
- Zero: this == other
- Positive: this > other

**Implementation:**

```kotlin
data class Person(val name: String, val age: Int) : Comparable<Person> {
    override fun compareTo(other: Person): Int {
        return this.age.compareTo(other.age)
    }
}
```

**Usage:**

```kotlin
val person1 = Person("Alice", 25)
val person2 = Person("Bob", 30)

println(person1 < person2)  // true
println(person1 > person2)  // false
println(person1 >= person2) // false
```

**Built-in Comparable Types:**

- Numbers (Int, Double, Float, etc.)
- Char
- String
- Dates

**Benefits:**

- Enable natural ordering
- Work with sorting functions
- Use comparison operators

[← Back to Contents](#content-list)

---

## Delegate Interfaces

### ReadOnlyProperty Interface

A generic interface for creating read-only (val) property delegates.

**Interface:**

```kotlin
interface ReadOnlyProperty<in T, out V> {
    operator fun getValue(thisRef: T, property: KProperty<*>): V
}
```

**Implementation:**

```kotlin
class LoggingProperty<T>(private val value: T) : ReadOnlyProperty<Any?, T> {
    override fun getValue(thisRef: Any?, property: KProperty<*>): T {
        println("Getting value of ${property.name}")
        return value
    }
}
```

**Usage:**

```kotlin
class Example {
    val name: String by LoggingProperty("John")
}

val example = Example()
println(example.name) // Logs: "Getting value of name"
```

**Use Cases:**

- Lazy initialization
- Logging property access
- Computed properties
- Value transformation before return

[← Back to Contents](#content-list)

---

### ReadWriteProperty Interface

A generic interface for creating read-write (var) property delegates.

**Interface:**

```kotlin
interface ReadWriteProperty<in T, V> {
    operator fun getValue(thisRef: T, property: KProperty<*>): V
    operator fun setValue(thisRef: T, property: KProperty<*>, value: V)
}
```

**Implementation:**

```kotlin
class ValidatedProperty(private var value: Int) : ReadWriteProperty<Any?, Int> {
    override fun getValue(thisRef: Any?, property: KProperty<*>): Int {
        return value
    }
    
    override fun setValue(thisRef: Any?, property: KProperty<*>, value: Int) {
        if (value >= 0) {
            this.value = value
        } else {
            throw IllegalArgumentException("Value must be positive")
        }
    }
}
```

**Usage:**

```kotlin
class Example {
    var age: Int by ValidatedProperty(25)
}

val example = Example()
example.age = 30  // OK
// example.age = -5  // Throws exception
```

**Use Cases:**

- Value validation
- Change notification
- Logging changes
- Transforming values

[← Back to Contents](#content-list)

---

### ObservableProperty Class

A generic class for creating properties that observe value changes.

**Definition:**

```kotlin
abstract class ObservableProperty<V>(initialValue: V) : ReadWriteProperty<Any?, V> {
    protected open fun afterChange(property: KProperty<*>, oldValue: V, newValue: V) {}
}
```

**Implementation:**

```kotlin
class MonitoredProperty<T>(initialValue: T) : ObservableProperty<T>(initialValue) {
    override fun afterChange(property: KProperty<*>, oldValue: T, newValue: T) {
        println("${property.name} changed from $oldValue to $newValue")
    }
}
```

**Usage:**

```kotlin
class Example {
    var name: String by MonitoredProperty("John")
}

val example = Example()
example.name = "Jane" // Prints: "name changed from John to Jane"
```

**Built-in Delegates:**

```kotlin
// Not null delegate
var name: String by Delegates.notNull()

// Observable with afterChange
var age: Int by Delegates.observable(0) { prop, old, new ->
    println("$old -> $new")
}

// Vetoable with beforeChange (can prevent change)
var score: Int by Delegates.vetoable(0) { prop, old, new ->
    new >= 0 // Only allow positive values
}
```

[← Back to Contents](#content-list)

---

## Generic Extension Function

Create extension functions with generic type parameters for flexible, reusable code.

**Syntax:**

```kotlin
fun <T> T.extensionName(): ReturnType {
    // function body
}
```

**Examples:**

**Generic Extension:**

```kotlin
fun <T> T.printWithType() {
    println("Value: $this, Type: ${this?.javaClass?.simpleName}")
}

123.printWithType()      // Value: 123, Type: Integer
"Hello".printWithType()  // Value: Hello, Type: String
```

**With Constraints:**

```kotlin
fun <T : Number> T.double(): Double {
    return this.toDouble() * 2
}

println(5.double())      // 10.0
println(3.14.double())   // 6.28
```

**Collection Extensions:**

```kotlin
fun <T> List<T>.secondOrNull(): T? {
    return if (this.size >= 2) this[1] else null
}

println(listOf(1, 2, 3).secondOrNull())  // 2
println(listOf(1).secondOrNull())         // null
```

**Multiple Type Parameters:**

```kotlin
fun <T, R> T.convertTo(converter: (T) -> R): R {
    return converter(this)
}

val length = "Hello".convertTo { it.length }  // 5
```

**Benefits:**

- Add functionality to any type
- Type-safe operations
- Chainable methods
- Reusable across different types

[← Back to Contents](#content-list)

---

## Quick Reference

### Generic Variance Summary

|Type|Keyword|Substitution|Usage|Example|
|---|---|---|---|---|
|**Invariant**|none|No substitution|Default|`class Box<T>`|
|**Covariant**|`out`|Child → Parent|Return types only|`class Producer<out T>`|
|**Contravariant**|`in`|Parent → Child|Parameters only|`class Consumer<in T>`|

### Common Patterns

**Generic Class:**

```kotlin
class Container<T>(val value: T)
```

**Generic Function:**

```kotlin
fun <T> identity(value: T): T = value
```

**Constrained Generic:**

```kotlin
fun <T : Comparable<T>> max(a: T, b: T): T =
    if (a > b) a else b
```

**Extension Function:**

```kotlin
fun <T> T.toList(): List<T> = listOf(this)
```

### Best Practices

1. **Use meaningful names** for type parameters when clarity helps
2. **Prefer `out`** for read-only/producer classes
3. **Prefer `in`** for write-only/consumer classes
4. **Use constraints** to ensure type safety
5. **Use star projection** when type doesn't matter
6. **Remember type erasure** - don't rely on runtime type info

---

**Next Topics:**

- Kotlin Collection
- Kotlin Coroutine

**Resources:**

- Website: www.programmerzamannow.com
- YouTube: youtube.com/c/ProgrammerZamanNow
- Telegram: @khannedy

[← Back to Contents](#content-list)