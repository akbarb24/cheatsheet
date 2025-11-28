**Author:** Eko Kurniawan Khannedy  
**Source:** Programmer Zaman Now

---

## 📋 Content List

1. [[#Introduction to Parallel & Concurrency Programming]]
2. [[#Thread & ExecutorService]]
3. [[#Introduction to Coroutine]]
4. [[#Job]]
5. [[#Async & Deferred]]
6. [[#Coroutine Context]]
7. [[#Coroutine Dispatcher]]
8. [[#Coroutine Scope]]
9. [[#Exception Handling]]
10. [[#Mutex & Semaphore]]
11. [[#Flow]]
12. [[#Channel]]
13. [[#Shared Flow & State Flow]]
14. [[#Advanced Topics]]

---

## Introduction to Parallel & Concurrency Programming

### Parallel Programming

Parallel programming is breaking down a problem into smaller parts and executing them simultaneously at the same time.

**Examples:**

- Running multiple applications simultaneously (office, editor, browser)
- Multiple chefs preparing different dishes in a restaurant
- Multiple tellers serving customers at a bank

**Process vs Thread:**

|Process|Thread|
|---|---|
|Execution of a program|Segment of a process|
|Consumes large memory|Uses small memory|
|Isolated from other processes|Can communicate within same process|
|Slow to start/stop|Fast to start/stop|

### Concurrency Programming

Concurrency is running multiple tasks by switching between them (time-slicing), not necessarily at the same time.

**Key Differences:**

- **Parallel**: Multiple tasks running simultaneously (needs multiple threads)
- **Concurrent**: Multiple tasks switching execution (can use fewer threads)

**Example:** Eating at a cafe - you eat, then talk, then drink, then eat again (one at a time, but switching between activities).

### CPU-bound vs I/O-bound

**CPU-bound:**

- Depends heavily on CPU speed
- Example: Machine Learning algorithms
- Best suited for **Parallel Programming**

**I/O-bound:**

- Depends on input/output device speed
- Example: Reading from database, file operations
- Best suited for **Concurrency Programming**
- Thread can do other work while waiting for I/O

[[#📋 Content List|← Back to Contents ]]

---

## Thread & ExecutorService

### Creating Threads

Kotlin uses Java Thread under the hood.

**Basic Thread Creation:**

```kotlin
Thread {
    println("Running in thread: ${Thread.currentThread().name}")
}.start()

// Or using Kotlin helper
thread(start = true) {
    println("Running in thread: ${Thread.currentThread().name}")
}
```

**Main Thread:**

- Every application runs in a main thread
- JUnit tests run in their own thread
- Android apps run in the UI thread

### ExecutorService

ExecutorService manages thread pools, avoiding the overhead of creating threads manually.

**Why Use ExecutorService?**

- Threads are heavy (512KB - 1MB each)
- Threads can be reused
- Better resource management

**Creating ExecutorService:**

```kotlin
// Single thread
val executor = Executors.newSingleThreadExecutor()

// Fixed thread pool
val executor = Executors.newFixedThreadPool(10)

// Cached thread pool (dynamic sizing)
val executor = Executors.newCachedThreadPool()

// Usage
executor.execute {
    println("Running task")
}
```

**ThreadPool:**

- Has an internal queue for tasks
- Tasks wait in queue until thread is available
- Efficient resource utilization

### Future & Callable

For tasks that return values, use `Callable` instead of `Runnable`.

**Callable Interface:**

```kotlin
val future: Future<String> = executor.submit(Callable {
    Thread.sleep(1000)
    "Result"
})

// Get result (blocks until complete)
val result = future.get()

// Check if done
if (future.isDone) { }

// Cancel task
future.cancel(true)
```

**Future Methods:**

- `get()` - Wait and get result
- `get(timeout, unit)` - Get with timeout
- `isDone()` - Check completion
- `cancel()` - Cancel task

[[#📋 Content List|← Back to Contents ]]

---

## Introduction to Coroutine

### What is Coroutine?

Coroutines are often called "lightweight threads," though they're not actually threads.

**Key Characteristics:**

- Execute inside threads
- Multiple coroutines can run in a single thread (concurrent)
- Cheap and fast to create (thousands or millions possible)
- Better memory efficiency than threads

**Problem with Java Threads:**

- Threads block when waiting
- Not designed for concurrency
- Cannot easily pause and resume

**Coroutine Solution:**

- Can suspend execution without blocking thread
- Thread can run other coroutines while one is suspended
- Inspired by Go-Lang Goroutines

### Suspend Function

Functions that can be paused and resumed without blocking the thread.

**Declaration:**

```kotlin
suspend fun doSomething() {
    delay(1000) // Suspends for 1 second (non-blocking)
    println("Done")
}
```

**Rules:**

- Must be called from another suspend function or coroutine
- Use `delay()` instead of `Thread.sleep()` for non-blocking delays

### Creating Coroutines

**Basic Coroutine:**

```kotlin
GlobalScope.launch {
    delay(1000)
    println("Coroutine finished")
}
```

**Blocking Main Thread:**

```kotlin
runBlocking {
    launch {
        delay(1000)
        println("World")
    }
    println("Hello")
}
```

**Coroutines are Lightweight:**

```kotlin
// Creating 100,000 coroutines (fast and efficient)
repeat(100_000) {
    GlobalScope.launch {
        delay(1000)
        print(".")
    }
}

// vs 100,000 threads (will crash or consume huge memory)
```

[[#📋 Content List|← Back to Contents ]]

---

## Job

Job is the handle to a coroutine, allowing control over its lifecycle.

### Job Operations

**Creating and Managing Jobs:**

```kotlin
val job = GlobalScope.launch {
    delay(1000)
    println("Coroutine done")
}

// Wait for completion
job.join()

// Check status
if (job.isActive) { }
if (job.isCompleted) { }
if (job.isCancelled) { }

// Cancel job
job.cancel()
```

### Cancelling Jobs

**Basic Cancellation:**

```kotlin
val job = GlobalScope.launch {
    delay(1000)
    println("This won't print if cancelled")
}

job.cancel()
job.join() // or use job.cancelAndJoin()
```

**Cancellable Coroutine:** To make coroutine cancellable, check `isActive`:

```kotlin
val job = GlobalScope.launch {
    while (isActive) { // Check if still active
        println("Working...")
        delay(100)
    }
    println("Cleaning up...")
}
```

**Cleanup with try-finally:**

```kotlin
val job = GlobalScope.launch {
    try {
        repeat(1000) {
            println("Working $it")
            delay(100)
        }
    } finally {
        println("Cleanup")
    }
}
```

### joinAll Function

Wait for multiple jobs to complete:

```kotlin
val job1 = launch { delay(1000) }
val job2 = launch { delay(2000) }
val job3 = launch { delay(3000) }

joinAll(job1, job2, job3)
// All jobs completed
```

### Timeout

Automatically cancel coroutine after timeout:

**With Exception:**

```kotlin
withTimeout(1000) {
    // Throws TimeoutCancellationException if exceeds 1 second
    longRunningTask()
}
```

**Without Exception:**

```kotlin
val result = withTimeoutOrNull(1000) {
    longRunningTask()
} // Returns null if timeout
```

[[#📋 Content List|← Back to Contents ]]

---

## Async & Deferred

### Sequential vs Concurrent

**Sequential (default):**

```kotlin
suspend fun getUser(): User { delay(1000); return User() }
suspend fun getProfile(): Profile { delay(1000); return Profile() }

runBlocking {
    val user = getUser()      // Takes 1s
    val profile = getProfile() // Takes 1s
    // Total: 2s
}
```

**Concurrent with launch (no return value):**

```kotlin
val job1 = launch { getUser() }
val job2 = launch { getProfile() }
joinAll(job1, job2)
// Total: 1s (parallel) but can't get return values
```

### Async Function

Like `launch` but returns `Deferred` which holds a result value.

**Using async:**

```kotlin
val deferredUser = async { getUser() }
val deferredProfile = async { getProfile() }

val user = deferredUser.await()      // Wait and get result
val profile = deferredProfile.await() // Wait and get result
// Total: 1s (parallel)
```

**Deferred:**

- Subclass of Job
- Contains a future value
- Similar to Promise or Future
- Use `await()` to get the value

### awaitAll Function

Wait for multiple Deferred values:

```kotlin
val deferred1 = async { getData1() }
val deferred2 = async { getData2() }
val deferred3 = async { getData3() }

val results: List<Data> = awaitAll(deferred1, deferred2, deferred3)
```

[[#📋 Content List|← Back to Contents ]]

---

## Coroutine Context

CoroutineContext is a collection of context elements that accompany coroutines.

**Main Elements:**

- **Job** - Coroutine lifecycle
- **CoroutineDispatcher** - Determines execution thread
- **CoroutineName** - Coroutine name for debugging
- **CoroutineExceptionHandler** - Exception handling

**Accessing Context:**

```kotlin
launch {
    println("Job: ${coroutineContext[Job]}")
    println("Dispatcher: ${coroutineContext[CoroutineDispatcher]}")
}
```

**Combining Elements:**

```kotlin
launch(Dispatchers.IO + CoroutineName("MyCoroutine")) {
    // Runs on IO dispatcher with custom name
}
```

[[#📋 Content List|← Back to Contents ]]

---

## Coroutine Dispatcher

Dispatcher determines which thread(s) execute the coroutine.

### Built-in Dispatchers

**Dispatchers.Default:**

- Minimum 2 threads or number of CPU cores (whichever is larger)
- For CPU-intensive tasks
- Default dispatcher if none specified

**Dispatchers.IO:**

- Thread pool that grows/shrinks as needed
- For I/O operations (network, file, database)
- Shares threads with Default dispatcher

**Dispatchers.Main:**

- Main UI thread (Android, JavaFX, Swing)
- Requires additional UI library dependency

**Dispatchers.Unconfined:**

- Doesn't confine to any specific thread
- Can switch threads during execution
- Not recommended for general use

### Using Dispatchers

```kotlin
// Default dispatcher
launch {
    println("Default: ${Thread.currentThread().name}")
}

// IO dispatcher
launch(Dispatchers.IO) {
    println("IO: ${Thread.currentThread().name}")
}

// Main dispatcher (requires dependency)
launch(Dispatchers.Main) {
    updateUI()
}
```

### Creating Custom Dispatcher

From ExecutorService:

```kotlin
val executor = Executors.newFixedThreadPool(10)
val dispatcher = executor.asCoroutineDispatcher()

launch(dispatcher) {
    println("Custom thread: ${Thread.currentThread().name}")
}

// Don't forget to close
dispatcher.close()
```

### withContext Function

Switch dispatcher within a coroutine:

```kotlin
launch(Dispatchers.Main) {
    // Running on Main thread
    
    val data = withContext(Dispatchers.IO) {
        // Switch to IO thread
        fetchDataFromNetwork()
    } // Automatically returns to Main thread
    
    updateUI(data)
}
```

**Use Cases:**

- Switch from Main to IO for network calls
- Switch from IO to Default for CPU-intensive work
- Keep UI updates on Main thread

[[#📋 Content List|← Back to Contents ]]

---

## Coroutine Scope

CoroutineScope defines the lifecycle boundary for coroutines.

### Why Use Scope?

**Problems with GlobalScope:**

- All coroutines share same scope
- Hard to cancel specific flows
- Not recommended for applications

**Benefits of Custom Scope:**

- Better lifecycle management
- Cancel all related coroutines together
- Logical grouping of coroutines

### Creating Scope

```kotlin
val scope = CoroutineScope(Dispatchers.IO)

scope.launch {
    // Coroutine 1
}

scope.launch {
    // Coroutine 2
}

// Cancel all coroutines in scope
scope.cancel()
```

### coroutineScope Function

Create temporary scope for grouping coroutines:

```kotlin
suspend fun loadData() = coroutineScope {
    val user = async { getUser() }
    val profile = async { getProfile() }
    
    Pair(user.await(), profile.await())
}
```

**Characteristics:**

- Creates child scope from parent
- If one coroutine fails, all siblings are cancelled
- Suspends until all children complete

### Parent-Child Relationship

**Child Scope Inherits:**

- Dispatcher from parent
- Context elements from parent

**Cancellation Propagation:**

- Cancelling parent cancels all children
- Parent waits for all children to complete

```kotlin
runBlocking {
    val parent = launch {
        val child1 = launch {
            delay(1000)
            println("Child 1")
        }
        
        val child2 = launch {
            delay(2000)
            println("Child 2")
        }
    }
    
    delay(500)
    parent.cancel() // Cancels both children too
}
```

### cancelChildren Function

Cancel only children, not parent:

```kotlin
val job = launch {
    launch { /* child 1 */ }
    launch { /* child 2 */ }
}

job.cancelChildren() // Only cancels children
job.join() // Parent still completes
```

### Naming Coroutines

For debugging purposes:

```kotlin
launch(CoroutineName("DataLoader")) {
    println("Running: ${coroutineContext[CoroutineName]}")
}
```

### yield Function

Give other coroutines a chance to run:

```kotlin
launch(Dispatchers.Default) {
    repeat(1000) {
        println("Coroutine A: $it")
        yield() // Let other coroutines run
    }
}

launch(Dispatchers.Default) {
    repeat(1000) {
        println("Coroutine B: $it")
        yield()
    }
}
```

**Benefits:**

- Cooperative multitasking
- Prevents coroutine from hogging dispatcher
- Automatically checks for cancellation

### awaitCancellation Function

Keep coroutine alive until cancelled:

```kotlin
val job = launch {
    try {
        awaitCancellation() // Suspends indefinitely
    } finally {
        println("Cancelled, cleaning up")
    }
}

delay(1000)
job.cancel()
```

[[#📋 Content List|← Back to Contents ]]

---

## Exception Handling

### Exception Propagation

**launch vs async:**

- **launch**: Exception thrown immediately, not exposed on `join()`
- **async**: Exception thrown when calling `await()`

**Example with launch:**

```kotlin
val job = launch {
    throw Exception("Error in launch")
}

try {
    job.join() // Exception not caught here
} catch (e: Exception) {
    // Won't catch the exception
}
```

**Example with async:**

```kotlin
val deferred = async {
    throw Exception("Error in async")
}

try {
    deferred.await() // Exception caught here
} catch (e: Exception) {
    println("Caught: ${e.message}")
}
```

### CoroutineExceptionHandler

Handle uncaught exceptions in coroutines:

```kotlin
val handler = CoroutineExceptionHandler { context, exception ->
    println("Caught: ${exception.message}")
}

val scope = CoroutineScope(Dispatchers.IO + handler)

scope.launch {
    throw Exception("Error")
    // Handler will catch this
}
```

**Important Notes:**

- Only works with `launch`, not `async`
- Must be installed in parent coroutine or scope
- CancellationException is not passed to handler

### Supervisor Job

**Regular Job:**

- If one child fails, all siblings are cancelled
- Error propagates to parent

**SupervisorJob:**

- Each child has independent lifecycle
- One child's failure doesn't affect siblings
- Error still reported to parent but doesn't cancel others

**Job Diagram:**

```
Job (parent)
├─ Child 1 (fails) ❌
├─ Child 2 (cancelled) ❌
└─ Child 3 (cancelled) ❌
```

**SupervisorJob Diagram:**

```
SupervisorJob (parent)
├─ Child 1 (fails) ❌
├─ Child 2 (continues) ✓
└─ Child 3 (continues) ✓
```

**Usage:**

```kotlin
val scope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

scope.launch {
    throw Exception("Error") // Only this fails
}

scope.launch {
    delay(1000)
    println("Still running") // This continues
}
```

### supervisorScope Function

Create supervisor scope without access to parent scope:

```kotlin
supervisorScope {
    launch {
        throw Exception("Error")
    }
    
    launch {
        delay(1000)
        println("Still running")
    }
}
```

**Exception Handler in supervisorScope:** Exception handlers work in child coroutines within supervisorScope:

```kotlin
supervisorScope {
    val handler = CoroutineExceptionHandler { _, e ->
        println("Caught: ${e.message}")
    }
    
    launch(handler) {
        throw Exception("Error") // Caught by handler
    }
}
```

[[#📋 Content List|← Back to Contents ]]

---

## Mutex & Semaphore

### Shared Mutable State Problem

**Race Condition:** Multiple coroutines accessing/modifying shared data simultaneously.

```kotlin
var counter = 0

repeat(1000) {
    launch {
        repeat(1000) {
            counter++ // Race condition!
        }
    }
}
// Final counter might not be 1,000,000
```

### Mutex

Mutual exclusion - ensures only one coroutine accesses code at a time.

**Using Mutex:**

```kotlin
val mutex = Mutex()
var counter = 0

repeat(1000) {
    launch {
        repeat(1000) {
            mutex.withLock {
                counter++ // Thread-safe
            }
        }
    }
}
// Counter will be exactly 1,000,000
```

**Manual Lock/Unlock:**

```kotlin
mutex.lock()
try {
    counter++
} finally {
    mutex.unlock()
}
```

**Key Points:**

- Only one coroutine can enter locked section
- Other coroutines wait (suspend) until unlocked
- Always unlock in finally block

### Semaphore

Like Mutex but allows multiple concurrent accesses:

```kotlin
val semaphore = Semaphore(permits = 3) // Allow 3 concurrent accesses

repeat(10) {
    launch {
        semaphore.withPermit {
            println("Working: $it")
            delay(1000)
        }
    }
}
// Only 3 coroutines run simultaneously
```

**Use Cases:**

- Rate limiting
- Resource pooling
- Limiting concurrent database connections
- Controlling API call rate

[[#📋 Content List|← Back to Contents ]]

---

## Flow

Flow is a cold asynchronous stream that emits multiple values sequentially.

### Creating Flow

**Basic Flow:**

```kotlin
fun numberFlow(): Flow<Int> = flow {
    repeat(10) {
        delay(100)
        emit(it) // Send value
    }
}

// Collect values
numberFlow().collect { value ->
    println(value)
}
```

**Flow Characteristics:**

- **Cold**: Doesn't execute until collected
- **Sequential**: Emits values one by one
- **Asynchronous**: Can use suspend functions

### Flow Operators

Similar to collection operators but support suspend functions:

**Transform Operators:**

```kotlin
flowOf(1, 2, 3, 4, 5)
    .map { it * 2 }        // Transform each value
    .filter { it > 5 }     // Filter values
    .take(2)               // Take first 2
    .collect { println(it) }
```

**Common Operators:**

- `map`, `filter`, `transform`
- `take`, `drop`, `takeWhile`, `dropWhile`
- `flatMapConcat`, `flatMapMerge`
- `zip`, `combine`
- `reduce`, `fold`
- `onEach`, `onStart`, `onCompletion`

### Flow Exception Handling

**try-catch:**

```kotlin
flow {
    emit(1)
    throw Exception("Error")
}
.collect {
    try {
        println(it)
    } catch (e: Exception) {
        println("Error: ${e.message}")
    }
}
```

**catch Operator:**

```kotlin
flow {
    emit(1)
    throw Exception("Error")
}
.catch { e ->
    println("Caught: ${e.message}")
    emit(-1) // Can emit fallback value
}
.collect { println(it) }
```

**onCompletion:**

```kotlin
flow {
    emit(1)
    emit(2)
}
.onCompletion { cause ->
    if (cause != null) {
        println("Completed with error: $cause")
    } else {
        println("Completed successfully")
    }
}
.collect { println(it) }
```

### Cancelling Flow

Flows are cancellable through coroutine scope:

```kotlin
val job = launch {
    flow {
        repeat(10) {
            delay(100)
            emit(it)
        }
    }.collect { println(it) }
}

delay(250)
job.cancel() // Cancels flow
```

**Flow automatically checks for cancellation** in built-in operators.

[[#📋 Content List|← Back to Contents ]]

---

## Channel

Channel is a communication pipeline between coroutines (hot stream).

### Basic Channel

**Creating and Using Channel:**

```kotlin
val channel = Channel<Int>()

// Producer
launch {
    repeat(5) {
        channel.send(it)
        println("Sent: $it")
    }
    channel.close()
}

// Consumer
launch {
    for (value in channel) {
        println("Received: $value")
    }
}
```

**Key Operations:**

- `send(value)` - Send value to channel (suspends if full)
- `receive()` - Receive value from channel (suspends if empty)
- `close()` - Close channel

### Channel Capacity

**Default (Rendezvous):**

```kotlin
val channel = Channel<Int>() // Capacity 0
// Sender blocks until receiver takes value
```

**Buffered:**

```kotlin
val channel = Channel<Int>(capacity = 10)
// Can send up to 10 values before blocking
```

**Unlimited:**

```kotlin
val channel = Channel<Int>(Channel.UNLIMITED)
// Never blocks sender
```

**Conflated:**

```kotlin
val channel = Channel<Int>(Channel.CONFLATED)
// Keeps only latest value
```

### Buffer Overflow Strategy

```kotlin
val channel = Channel<Int>(
    capacity = 5,
    onBufferOverflow = BufferOverflow.DROP_OLDEST
)
```

**Strategies:**

- `SUSPEND` - Block sender (default)
- `DROP_OLDEST` - Remove oldest value in buffer
- `DROP_LATEST` - Remove newest value in buffer

### Undelivered Element Handler

Handle values sent to closed channel:

```kotlin
val channel = Channel<Int> { undelivered ->
    println("Undelivered: $undelivered")
}

launch {
    channel.send(1)
    channel.close()
    channel.send(2) // Calls handler with value 2
}
```

### produce Function

Create channel with coroutine builder:

```kotlin
val channel: ReceiveChannel<Int> = produce {
    repeat(5) {
        send(it)
    }
} // Automatically closed

for (value in channel) {
    println(value)
}
```

### Broadcast Channel

Channel with multiple receivers:

```kotlin
val channel = BroadcastChannel<Int>(Channel.BUFFERED)

// Multiple receivers
val receiver1 = channel.openSubscription()
val receiver2 = channel.openSubscription()

launch {
    for (value in receiver1) {
        println("Receiver 1: $value")
    }
}

launch {
    for (value in receiver2) {
        println("Receiver 2: $value")
    }
}

// Send to all receivers
channel.send(1)
channel.send(2)
```

**Note:** BroadcastChannel is deprecated, use SharedFlow instead.

### broadcast Function

```kotlin
val channel = broadcast {
    repeat(5) {
        send(it)
    }
}
```

### Conflated Broadcast Channel

Only latest value received:

```kotlin
val channel = ConflatedBroadcastChannel<Int>()

channel.openSubscription() // Only gets latest value
```

### Actor

Coroutine that acts as channel receiver:

```kotlin
val actor = actor<Int> {
    for (value in channel) {
        println("Processing: $value")
    }
}

actor.send(1)
actor.send(2)
actor.close()
```

### ticker Function

Create timer channel:

```kotlin
val ticker = ticker(delayMillis = 1000, initialDelayMillis = 0)

launch {
    for (event in ticker) {
        println("Tick: ${System.currentTimeMillis()}")
    }
}

delay(5000)
ticker.cancel()
```

[[#📋 Content List|← Back to Contents ]]

---

## Shared Flow & State Flow

### Shared Flow

Hot flow that can have multiple collectors.

**Creating Shared Flow:**

```kotlin
val sharedFlow = MutableSharedFlow<Int>()

// Collector 1
launch {
    sharedFlow.collect {
        println("Collector 1: $it")
    }
}

// Collector 2
launch {
    sharedFlow.collect {
        println("Collector 2: $it")
    }
}

// Emit values
sharedFlow.emit(1)
sharedFlow.emit(2)
```

**Characteristics:**

- **Hot**: Emits immediately, doesn't wait for collectors
- **Multiple collectors**: All collectors receive values
- **Replays**: Can replay values to new collectors

**Configuration:**

```kotlin
val sharedFlow = MutableSharedFlow<Int>(
    replay = 1,           // Replay last 1 value to new collectors
    extraBufferCapacity = 5, // Buffer capacity
    onBufferOverflow = BufferOverflow.DROP_OLDEST
)
```

**Shared Flow vs Broadcast Channel:**

- SharedFlow is Flow-based (supports operators)
- No close operation
- Better configurability
- Recommended replacement for BroadcastChannel

### State Flow

Shared flow that holds and emits current state.

**Creating State Flow:**

```kotlin
val stateFlow = MutableStateFlow(0) // Initial value

launch {
    stateFlow.collect {
        println("State: $it")
    }
}

stateFlow.value = 1  // Update state
stateFlow.value = 2
stateFlow.emit(3)
```

**Characteristics:**

- **Always has value**: Current state always available via `value`
- **Conflated**: New collectors only get latest value
- **Distinct values**: Only emits when value actually changes

**Use Cases:**

- UI state management
- Configuration state
- User session state
- Any scenario where current state matters

**Accessing State:**

```kotlin
println("Current state: ${stateFlow.value}")
```

**State Flow vs Conflated Broadcast Channel:**

- StateFlow is recommended replacement
- Better integration with Flow operators
- Clearer semantics for state management

[[#📋 Content List|← Back to Contents ]]

---

## Advanced Topics

### select Function

Wait for the first result from multiple suspending operations.

**With Deferred:**

```kotlin
val deferred1 = async { delay(1000); "Result 1" }
val deferred2 = async { delay(500); "Result 2" }

val result = select<String> {
    deferred1.onAwait { it }
    deferred2.onAwait { it }
}

println(result) // "Result 2" (faster)
```

**With Channel:**

```kotlin
val channel1 = Channel<Int>()
val channel2 = Channel<Int>()

launch { channel1.send(1) }
launch { channel2.send(2) }

val result = select<Int> {
    channel1.onReceive { it }
    channel2.onReceive { it }
}

println(result) // Whichever arrives first
```

**Use Cases:**

- Timeout fallback
- Racing multiple data sources
- First response wins scenarios

### Non-Cancellable Context

Execute code that shouldn't be cancelled:

```kotlin
val job = launch {
    try {
        repeat(1000) {
            println("Working...")
            delay(100)
        }
    } finally {
        withContext(NonCancellable) {
            // This will complete even if job is cancelled
            delay(500)
            println("Cleanup completed")
        }
    }
}

delay(500)
job.cancel()
```

**Use Cases:**

- Critical cleanup operations
- Logging after cancellation
- Releasing resources that must be released

[[#📋 Content List|← Back to Contents ]]

---

## Quick Reference

### Coroutine Builders

|Builder|Return Type|Purpose|
|---|---|---|
|`launch`|Job|Fire-and-forget, no result|
|`async`|Deferred<T>|Returns result|
|`runBlocking`|T|Blocks current thread|
|`produce`|ReceiveChannel<T>|Creates channel producer|
|`actor`|SendChannel<T>|Creates channel consumer|

### Dispatchers

|Dispatcher|Use Case|
|---|---|
|`Dispatchers.Default`|CPU-intensive work|
|`Dispatchers.IO`|I/O operations (network, disk, DB)|
|`Dispatchers.Main`|UI updates (Android, JavaFX)|
|`Dispatchers.Unconfined`|Not confined to specific thread|

### Scope Functions

|Function|Purpose|
|---|---|
|`coroutineScope`|Creates child scope, waits for children|
|`supervisorScope`|Creates supervisor child scope|
|`withContext`|Switches dispatcher/context|
|`withTimeout`|Executes with timeout (throws)|
|`withTimeoutOrNull`|Executes with timeout (returns null)|

### Flow vs Channel vs SharedFlow

|Feature|Flow|Channel|SharedFlow|
|---|---|---|---|
|Hot/Cold|Cold|Hot|Hot|
|Multiple collectors|No|No|Yes|
|Buffering|Operators|Built-in|Configurable|
|Close operation|No|Yes|No|
|Operators|Yes|No|Yes|

### Best Practices

1. **Avoid GlobalScope** - Use structured concurrency
2. **Use appropriate dispatcher** - IO for I/O, Default for CPU
3. **Use SupervisorJob** for independent child lifecycles
4. **Always handle exceptions** - Use try-catch or CoroutineExceptionHandler
5. **Prefer immutable data** - Avoid shared mutable state
6. **Use Mutex/Semaphore** for shared mutable state when necessary
7. **Cancel coroutines** when no longer needed
8. **Use Flow** for streams of values
9. **Use StateFlow** for state management
10. **Name coroutines** for easier debugging

### Common Patterns

**Parallel Execution:**

```kotlin
coroutineScope {
    val result1 = async { fetchData1() }
    val result2 = async { fetchData2() }
    combine(result1.await(), result2.await())
}
```

**Error Handling:**

```kotlin
supervisorScope {
    val handler = CoroutineExceptionHandler { _, e ->
        log.error("Error: $e")
    }
    
    launch(handler) { riskyOperation() }
}
```

**State Management:**

```kotlin
class ViewModel {
    private val _state = MutableStateFlow(InitialState)
    val state: StateFlow<State> = _state.asStateFlow()
    
    fun updateState(newState: State) {
        _state.value = newState
    }
}
```

**Resource Cleanup:**

```kotlin
val job = launch {
    try {
        doWork()
    } finally {
        withContext(NonCancellable) {
            cleanup()
        }
    }
}
```

---

**Next Topics:**

- Android Development
- Backend Development with Kotlin

**Resources:**

- Website: www.programmerzamannow.com
- YouTube: youtube.com/c/ProgrammerZamanNow
- Telegram: @khannedy

[[#📋 Content List|← Back to Contents ]]