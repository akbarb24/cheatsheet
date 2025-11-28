**Author:** Eko Kurniawan Khannedy  
**Source:** Programmer Zaman Now

---

## 📋 Content List

1. [[#Introduction to Collection]]
2. [[#List]]
3. [[#Set]]
4. [[#Pair]]
5. [[#Map]]
6. [[#Collection Interface]]
7. [[#Iterable]]
8. [[#Iterator]]
9. [[#Collection Conversion]]
10. [[#Collection Operations]]
11. [[#Transformations]]
    - [[#Mapping]]
    - [[#Zipping]]
    - [[#Association]]
    - [[#Flattening]]
    - [[#String Representation]]
12. [[#Filtering]]
13. [[#Plus & Minus Operators]]
14. [[#Grouping]]
15. [[#Slice Operations]]
16. [[#Retrieving Elements]]
17. [[#Ordering]]
18. [[#Aggregate Operations]]
19. [[#Sequence]]
20. [[#Specific Operations]]

---

## Introduction to Collection

Collections are fundamental data structures that store multiple elements. Kotlin provides a rich standard library with built-in collection types.

### Types of Collections

- **Immutable**: Read-only collections (List, Set, Map)
- **Mutable**: Collections with write operations (MutableList, MutableSet, MutableMap)

**Key Points:**

- Collections can contain zero or more elements
- All collection types are available in the Kotlin standard library
- Two main categories: Immutable (read-only) and Mutable (read/write)

[[#📋 Content List|← Back to Contents]]

---

## List

An ordered collection that allows duplicate elements and provides index-based access, similar to arrays.

**Common Functions:**

- `listOf()` - Create immutable list
- `mutableListOf()` - Create mutable list
- `get(index)` or `[index]` - Access element by index
- `indexOf()`, `lastIndexOf()` - Find element position
- `add()`, `remove()`, `clear()` - Mutable operations

**Use Cases:**

- Storing ordered data
- When duplicates are allowed
- Index-based access is needed

[[#📋 Content List|← Back to Contents]]

---

## Set

An unordered collection that stores unique elements only. Duplicates are automatically removed.

**Common Functions:**

- `setOf()` - Create immutable set
- `mutableSetOf()` - Create mutable set
- `contains()` - Check if element exists
- `add()`, `remove()` - Mutable operations
- `union()`, `intersect()`, `subtract()` - Set operations

**Key Points:**

- Uses `hashCode()` and `equals()` to determine uniqueness
- Perfect for storing unique data
- No guaranteed order

[[#📋 Content List|← Back to Contents]]

---

## Pair

A simple data structure that holds two related values.

**Properties:**

- `first` - First value
- `second` - Second value

**Creation:**

```kotlin
Pair(key, value)
key to value  // infix notation
```

**Use Cases:**

- Returning two values from a function
- Creating Map entries
- Temporary data grouping

[[#📋 Content List|← Back to Contents]]

---

## Map

A collection of key-value pairs where each key is unique. Also known as a dictionary.

**Common Functions:**

- `mapOf()` - Create immutable map
- `mutableMapOf()` - Create mutable map
- `get(key)` or `[key]` - Access value by key
- `keys`, `values`, `entries` - Access components
- `put()`, `remove()` - Mutable operations

**Key Points:**

- Keys must be unique
- Duplicate keys will replace old values
- Any data type can be used as key or value

[[#📋 Content List|← Back to Contents]]

---

## Collection Interface

The base interface for all collection types, providing general operations for reading and writing data.

**Common Functions:**

- `size` - Number of elements
- `isEmpty()` - Check if empty
- `contains()` - Check if element exists
- `containsAll()` - Check if all elements exist
- `iterator()` - Get iterator

**Hierarchy:**

- All List, Set, and Map extend from Collection
- MutableCollection adds write operations

[[#📋 Content List|← Back to Contents]]

---

## Iterable

The superclass of Collection interface, providing general operations for iterating through elements.

**Common Functions:**

- `iterator()` - Get iterator
- `forEach()` - Iterate with lambda
- `forEachIndexed()` - Iterate with index

**Key Points:**

- Base interface for all iterable collections
- Enables for-loop functionality
- MutableIterable adds removal during iteration

[[#📋 Content List|← Back to Contents]]

---

## Iterator

Provides iteration capabilities with different types for different collections.

**Types:**

- `Iterator` - Basic iteration
- `MutableIterator` - Iteration with removal
- `ListIterator` - Bidirectional iteration for List
- `MutableListIterator` - Bidirectional with modification

**Key Functions:**

- `hasNext()` - Check if more elements exist
- `next()` - Get next element
- `remove()` - Remove current element (mutable)
- `hasPrevious()`, `previous()` - For ListIterator

[[#📋 Content List|← Back to Contents]]

---

## Collection Conversion

Easily convert between different collection types using conversion functions.

**Common Conversions:**

- `toList()` - Convert to List
- `toSet()` - Convert to Set
- `toMap()` - Convert to Map
- `toMutableList()`, `toMutableSet()`, `toMutableMap()` - Convert to mutable
- Array to Collection and vice versa

**Example Pattern:**

```kotlin
arrayOf(1,2,3).toList()
setOf(1,2,3).toMutableList()
```

[[#📋 Content List|← Back to Contents]]

---

## Collection Operations

Kotlin provides extensive extension functions for collection operations. These operations are safe as they create new collections without modifying the original.

**Operation Categories:**

1. Transformations
2. Filtering
3. Plus/Minus operators
4. Grouping
5. Retrieving parts
6. Retrieving elements
7. Ordering
8. Aggregate operations

**Key Principle:**

- Operations return new collections
- Original collection remains unchanged
- Safe for immutable programming

[[#📋 Content List|← Back to Contents]]

---

## Transformations

### Mapping

Transform each element in a collection to create a new collection.

**Functions:**

- `map { }` - Transform each element
- `mapIndexed { index, element -> }` - With index
- `mapNotNull { }` - Ignore null results
- `mapKeys { }` - Transform Map keys
- `mapValues { }` - Transform Map values

**Example:**

```kotlin
listOf(1,2,3).map { it * 2 } // [2,4,6]
```

[[#📋 Content List|← Back to Contents]]

---

### Zipping

Combine two collections into pairs or custom transformations.

**Functions:**

- `zip(other)` - Create Pair collection
- `zip(other) { a, b -> }` - Custom transform
- `unzip()` - Split Pair collection into two

**Example:**

```kotlin
listOf(1,2,3).zip(listOf("a","b","c"))
// [(1,a), (2,b), (3,c)]
```

[[#📋 Content List|← Back to Contents]]

---

### Association

Transform collections into Maps.

**Functions:**

- `associate { element -> key to value }` - Create Map
- `associateWith { element -> value }` - Element as key
- `associateBy { element -> key }` - Element as value

**Example:**

```kotlin
listOf("a","bb","ccc").associateWith { it.length }
// {a=1, bb=2, ccc=3}
```

[[#📋 Content List|← Back to Contents]]

---

### Flattening

Convert nested collections into flat collections.

**Functions:**

- `flatten()` - Flatten nested collection
- `flatMap { }` - Transform and flatten

**Example:**

```kotlin
listOf(listOf(1,2), listOf(3,4)).flatten()
// [1,2,3,4]
```

[[#📋 Content List|← Back to Contents]]

---

### String Representation

Convert collections to formatted strings.

**Functions:**

- `joinToString(separator, prefix, suffix)` - Basic join
- `joinToString(separator, prefix, suffix) { transform }` - With transform
- `joinTo(Appendable, ...)` - Append to existing string

**Example:**

```kotlin
listOf(1,2,3).joinToString(", ", "[", "]")
// "[1, 2, 3]"
```

[[#📋 Content List|← Back to Contents]]

---

## Filtering

Filter collections based on conditions (predicates).

**Common Functions:**

- `filter { condition }` - Keep matching elements
- `filterIndexed { index, element -> }` - With index
- `filterNot { condition }` - Keep non-matching
- `filterIsInstance<Type>()` - Filter by type
- `filterNotNull()` - Remove nulls

**Partitioning:**

- `partition { condition }` - Split into matching and non-matching

**Testing:**

- `any { condition }` - At least one matches
- `none { condition }` - None match
- `all { condition }` - All match

[[#📋 Content List|← Back to Contents]]

---

## Plus & Minus Operators

Add or remove elements/collections creating new collections.

**Functions:**

- `plus(element)` - Add element
- `plus(collection)` - Add collection
- `minus(element)` - Remove element
- `minus(collection)` - Remove collection

**Operator Syntax:**

```kotlin
list + element
list - element
list1 + list2
```

[[#📋 Content List|← Back to Contents]]

---
## Grouping

Group collection elements into categories.

**Functions:**

- `groupBy { keySelector }` - Returns Map<K, List<T>>
- `groupingBy { keySelector }` - Returns Grouping<K, T>

**Grouping Interface Operations:**

- `eachCount()` - Count elements per group
- `reduce()`, `fold()` - Aggregate per group
- `aggregate()` - Custom aggregation

**Example:**

```kotlin
listOf("a","bb","ccc").groupBy { it.length }
// {1=[a], 2=[bb], 3=[ccc]}
```

[[#📋 Content List|← Back to Contents]]

---

## Slice Operations

Extract portions of collections.

**Slice:**

- `slice(range)` - Get elements by index range

**Take:**

- `take(n)` - First n elements
- `takeLast(n)` - Last n elements
- `takeWhile { condition }` - While condition is true
- `takeLastWhile { condition }` - From end while true

**Drop:**

- `drop(n)` - Remove first n elements
- `dropLast(n)` - Remove last n elements
- `dropWhile { condition }` - Remove while condition is true
- `dropLastWhile { condition }` - From end while true

**Chunked:**

- `chunked(size)` - Split into chunks

**Windowed:**

- `windowed(size, step, partialWindow)` - Sliding window

[[#📋 Content List|← Back to Contents]]

---

## Retrieving Elements

Get single elements from collections.

**By Position:**

- `elementAt(index)` - At specific index
- `first()`, `last()` - First/last element
- `elementAtOrNull(index)` - Safe access
- `elementAtOrElse(index) { default }` - With default

**By Condition:**

- `first { condition }` - First matching
- `last { condition }` - Last matching
- `firstOrNull { }` or `find { }` - Safe first
- `lastOrNull { }` or `findLast { }` - Safe last

**Random:**

- `random()` - Random element

**Checking Existence:**

- `contains(element)` - Check if exists
- `containsAll(collection)` - Check all exist
- `isEmpty()`, `isNotEmpty()` - Check if empty

[[#📋 Content List|← Back to Contents]]

---

## Ordering

Sort collections in various ways.

**Natural Order:**

- `sorted()` - Ascending order
- `sortedDescending()` - Descending order

**Custom Order:**

- `sortedBy { selector }` - Sort by property (ascending)
- `sortedByDescending { selector }` - Sort by property (descending)
- `sortedWith(comparator)` - Custom comparator

**Reverse:**

- `reversed()` - New reversed collection
- `asReversed()` - Reversed view (updates with original)

**Random:**

- `shuffled()` - Random order

[[#📋 Content List|← Back to Contents]]

---

## Aggregate Operations

Perform calculations on collection data.

**Basic Aggregates:**

- `max()`, `min()` - Maximum/minimum value
- `average()` - Average value
- `sum()` - Sum of all elements
- `count()` - Number of elements

**With Selector:**

- `maxBy { selector }`, `minBy { selector }` - By property
- `maxWith(comparator)`, `minWith(comparator)` - By comparator
- `sumBy { selector }` - Sum by property
- `sumByDouble { selector }` - Sum as Double

**Manual Aggregation:**

- `reduce { accumulator, element -> }` - Fold without initial value
- `fold(initial) { accumulator, element -> }` - Fold with initial value
- `reduceRight()`, `foldRight()` - From end
- `reduceIndexed()`, `foldIndexed()` - With index

[[#📋 Content List|← Back to Contents]]

---

## Sequence

A collection type that evaluates operations lazily for better performance with large datasets.

**Key Differences:**

- **Collection**: Eager evaluation (each operation creates new collection)
- **Sequence**: Lazy evaluation (operations execute only when needed)

**When to Use:**

- ✅ Large datasets
- ✅ Complex, multiple operations
- ❌ Small datasets (overhead not worth it)
- ❌ Simple operations

**Creation:**

```kotlin
listOf(1,2,3).asSequence()
sequenceOf(1,2,3)
generateSequence { }
```

**Key Point:** Operations on Sequence are only executed when a terminal operation (like `toList()`, `count()`) is called.

[[#📋 Content List|← Back to Contents]]

---

## Specific Operations

### List Specific Operations

**Functions:**

- `getOrElse(index) { default }` - Safe get with default
- `getOrNull(index)` - Safe get
- `subList(from, to)` - Get sublist
- `binarySearch(value)` - Binary search
- `indexOf(value)`, `lastIndexOf(value)` - Find index
- `indexOfFirst { }`, `indexOfLast { }` - Find by condition

### Set Specific Operations

**Functions:**

- `union(other)` - All elements from both sets
- `intersect(other)` - Common elements
- `subtract(other)` - Elements not in other set

### Map Specific Operations

**Functions:**

- `getOrElse(key) { default }` - Safe get with default
- `getValue(key)` - Get or throw exception
- `filterKeys { }` - Filter by key condition
- `filterValues { }` - Filter by value condition

### Map Properties & Destructuring

**Delegate Properties:**

```kotlin
val map = mapOf("name" to "John")
val name by map  // Delegate to map
```

**Destructuring:**

```kotlin
for ((key, value) in map) { }
```
[[#📋 Content List|← Back to Contents]]

---

## Quick Reference

### Collection Creation

```kotlin
// Immutable
listOf(1,2,3)
setOf(1,2,3)
mapOf(1 to "a", 2 to "b")

// Mutable
mutableListOf(1,2,3)
mutableSetOf(1,2,3)
mutableMapOf(1 to "a", 2 to "b")
```

### Common Patterns

```kotlin
// Transform
list.map { it * 2 }

// Filter
list.filter { it > 5 }

// Group
list.groupBy { it % 2 }

// Aggregate
list.sum()
list.reduce { acc, i -> acc + i }
```
[[#📋 Content List|← Back to Contents]]

---

**Next Topics:**

- Gradle
- Kotlin Unit Test
- Kotlin Coroutine

**Resources:**

- Website: www.programmerzamannow.com
- YouTube: youtube.com/c/ProgrammerZamanNow
- Telegram: @khannedy

[↑ Back to Content List](https://claude.ai/chat/9a588d5d-eaa5-4a76-a9bf-4f4bf7ef9c62#-content-list)