conda activate pyproject
conda deactivate

# threading.Condition().notify()

在Python的`threading`模块中，`Condition`
对象用于线程之间的同步，特别是当需要多个线程在某些条件成立时才能继续执行时。`Condition`对象内部维护了一个锁（通常是`RLock`
），并且支持等待/通知机制。这意味着线程可以在等待某个条件变为真时阻塞，而当条件满足时，另一个线程可以通知一个或多个等待的线程继续执行。

`Condition`对象的`notify()`方法用于唤醒正在等待该条件的单个线程。这意味着，如果有多个线程在等待同一个条件，`notify()`
只会唤醒它们中的一个。哪个线程被唤醒取决于操作系统的调度策略，因此是不可预测的。

下面是一个简单的例子，展示了如何使用`Condition`对象以及`notify()`方法：

```python
import threading

# 定义一个条件变量
condition = threading.Condition()

# 定义一个标志变量，用于控制线程的执行
shared_flag = False


def worker():
    global shared_flag
    # 线程首先获取条件变量的锁
    with condition:
        # 等待条件满足（shared_flag为True）
        while not shared_flag:
            condition.wait()  # 如果没有条件满足，则阻塞当前线程
        print(f"Thread {threading.current_thread().name} is running.")


# 创建并启动多个线程
threads = [threading.Thread(target=worker, name=f'Thread-{i}') for i in range(3)]
for t in threads:
    t.start()

# 假设在某个时间点，条件满足了
import time

time.sleep(1)  # 假设的延时，实际场景中可能是某种条件的达成

# 修改标志变量，并通知等待的线程
with condition:
    shared_flag = True
    condition.notify()  # 唤醒一个等待的线程

# 注意：这里只唤醒了一个线程。如果要唤醒所有等待的线程，应该使用notify_all()方法。
```

需要注意的是，`notify()`
方法只是发送了一个通知，它并不保证等待的线程会立即被唤醒。等待的线程只有在重新尝试获取条件变量的锁时才会被唤醒（这发生在`condition.wait()`
调用之后）。此外，由于只唤醒了一个线程，所以如果需要唤醒所有等待的线程，应该使用`condition.notify_all()`方法。

最后，务必确保在调用`notify()`或`notify_all()`之前已经获得了条件变量的锁，否则将抛出`RuntimeError`
异常。在上面的例子中，我们通过在`with condition:`块中调用`notify()`来确保这一点。

# with语句

Python 中的 `with` 语句是一种上下文管理器（context
manager），它用于包装代码的执行，以便在代码执行前后自动执行某些操作，比如资源的获取与释放、文件的打开与关闭等。使用 `with`
语句可以简化代码，并自动处理资源释放等清理工作，即使在发生异常时也能保证资源被正确释放。

### 基本用法

`with` 语句的基本语法如下：

```python
with expression as variable:
    with-block
```

- `expression` 必须是一个上下文管理器对象，它必须实现 `__enter__()` 和 `__exit__()` 这两个方法。
- `as variable` 是可选的，如果提供，`__enter__()` 方法的返回值将被赋值给 `variable`。
- `with-block` 是 `with` 语句下的代码块，执行完毕后，无论是否发生异常，都会执行 `__exit__()` 方法。

### 示例

#### 文件操作

使用 `with` 语句打开文件，可以自动关闭文件，即使发生异常也是如此。

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# 文件在这里自动关闭
```

#### 线程锁

在多线程编程中，可以使用 `with` 语句来自动管理锁的获取与释放。

```python
import threading

lock = threading.Lock()

with lock:
    # 临界区代码
    print("Critical section")
# 锁在这里自动释放
```

### 自定义上下文管理器

你可以通过定义一个类，并实现 `__enter__()` 和 `__exit__()` 方法来创建自定义的上下文管理器。

```python
class MyContextManager:
    def __enter__(self):
        print("Entering")
        # 返回的资源，可以赋值给 as 子句中的变量
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
        # 如果需要，可以在这里处理异常
        # 如果处理了异常，应该返回 True
        # 否则，返回 False
        return False


with MyContextManager() as cm:
    print("Inside the context manager")
# 输出:
# Entering
# Inside the context manager
# Exiting
```

`__exit__` 方法接收三个参数，分别代表异常类型、异常值和异常跟踪信息。如果没有异常发生，这三个参数都将为 `None`
。如果 `__exit__` 方法返回 `True`，则异常会被忽略（即被处理）；如果返回 `False` 或不返回任何值（默认为 `None`），则异常会被正常抛出。

# os

## os.makedirs

`os.makedirs` 是 Python 中 `os` 模块的一个函数，用于递归地创建目录。这意味着如果目标目录的上级目录不存在，`os.makedirs`
会先创建上级目录，直到创建出完整的路径。这对于需要创建多层嵌套目录的场景非常有用。

### 函数原型

```python
os.makedirs(name, mode=0o777, exist_ok=False)
```

- `name`：需要创建的目录的完整路径。
- `mode`：目录的权限模式（数字模式），默认为 `0o777`（八进制表示，表示目录对所有用户可读、可写、可执行）。然而，这个模式会受到当前进程的
  umask（用户文件创建掩码）的影响。umask 会从 `mode` 中移除一些权限位。
- `exist_ok`：一个布尔值，表示如果目录已存在，是否引发异常。如果 `exist_ok` 为 `True`
  ，并且目录已存在，则不会引发异常；如果为 `False`（默认值），并且目录已存在，则会引发 `FileExistsError` 异常。

### 示例

#### 基本用法

```python
import os

# 假设我们要创建多级目录 /tmp/a/b/c
os.makedirs('/tmp/a/b/c')

# 现在 /tmp/a/b/c 目录及其所有上级目录都已创建
```

#### 设置目录权限和避免异常

```python
import os

# 尝试创建目录，并设置权限，如果目录已存在，则忽略异常
try:
    os.makedirs('/tmp/a/b/c', mode=0o755, exist_ok=True)
except FileExistsError:
    print("目录已存在，忽略...")

# 现在，如果 /tmp/a/b/c 不存在，它会被创建，并且权限被设置为 0o755
# 如果目录已存在，则不会引发异常
```

注意：权限设置（`mode` 参数）可能会受到运行 Python 脚本的用户或系统的 umask
设置的影响。因此，实际创建的目录权限可能与指定的 `mode` 参数不完全相同。

### 注意事项

- 在使用 `os.makedirs` 时，请确保你有足够的权限来创建目录。
- 如果你的应用场景需要处理大量的文件或目录创建，考虑异常处理来避免程序因为权限问题或目录已存在而中断。
- 在某些环境中（如 Unix/Linux 系统），目录权限的设置可能受到 umask 的影响，因此实际权限可能与预期不同。

# shutil.move

`shutil.move` 是 Python 中 `shutil`
模块的一个函数，用于移动文件或目录到新的位置。如果目标位置是一个已经存在的目录，那么文件或目录将被移动到该目录下。如果目标位置是一个文件，并且已经存在，它将被替换。这个函数提供了一种方便的方式来重命名文件或目录，或者将它们移动到不同的位置。

### 函数原型

```python
shutil.move(src, dst, *, copy_function=copy2)
```

- `src`：源文件或目录的路径。
- `dst`：目标路径，可以是文件或目录的路径。
- `copy_function`：一个可选参数，指定用于复制文件或目录的函数。默认是 `copy2`，它类似于 `shutil.copy2`
  ，会保留文件的元数据（如修改时间和访问权限）。这个参数通常不需要更改，除非你有特殊的需求。

### 注意事项

- 如果 `dst` 是一个目录，那么 `src` 将会被移动到该目录下，并保持原名。
- 如果 `dst` 是一个文件并且已经存在，它将被 `src` 替换。
- 如果 `dst` 是一个不存在的路径（既不是文件也不是目录），则根据 `dst`
  的格式，它会被视为一个文件或目录的完整路径，并创建相应的文件或目录来存放 `src`。
- 默认情况下，如果 `src` 和 `dst` 在同一个文件系统上，`shutil.move` 将会尝试使用操作系统提供的重命名操作（如 Unix
  的 `rename`），这通常比复制和删除要快得多。如果 `src` 和 `dst`
  在不同的文件系统上，或者出于某种原因重命名操作不可行，`shutil.move` 将会回退到使用 `copy_function`（默认为 `copy2`
  ）来复制文件，然后删除原始文件。

### 示例

#### 移动文件

```python
import shutil

# 移动文件
shutil.move('source.txt', 'destination.txt')

# 或者，将文件移动到新的目录
shutil.move('source.txt', '/path/to/new/directory/source.txt')
```

#### 移动目录

```python
import shutil

# 假设 'old_dir' 是一个存在的目录
shutil.move('old_dir', 'new_dir')

# 这将把 'old_dir' 及其所有内容移动到 'new_dir'
# 注意：'new_dir' 不能是一个已存在的目录，否则会引发异常（除非设置了 exist_ok=True，但 shutil.move 没有这个参数）
# 如果需要处理已存在的目标目录，你可能需要先删除它或使用其他逻辑
```

请注意，`shutil.move` 没有直接的 `exist_ok`
参数来处理目标路径已存在的情况。如果你需要这种功能，你可能需要手动检查目标路径是否存在，并根据需要处理它（例如，删除目标文件或目录，或者选择一个不同的目标路径）。然而，对于文件来说，如果目标路径是一个已存在的文件，`shutil.move`
会直接替换它。

# pandas

## pandas.read_csv

`pandas.read_csv()` 是 Pandas 库中用于读取 CSV（逗号分隔值）文件并将其转换为 DataFrame 对象的函数。DataFrame 是 Pandas
中一种非常重要的数据结构，它以表格形式存储数据，其中可以包含多种数据类型（数值、字符串、布尔值等），并且支持丰富的数据操作和分析功能。

### 基本用法

```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('file_path.csv')

# 显示前几行数据，默认是前5行
print(df.head())
```

其中 `'file_path.csv'` 是你想要读取的 CSV 文件的路径。如果文件位于你的当前工作目录中，你只需提供文件名；否则，你需要提供完整的文件路径。

### 常用参数

- `sep` 或 `delimiter`：指定字段之间的分隔符，默认为逗号 `','`。如果你的 CSV 文件是用其他字符（如制表符 `\t`）分隔的，你需要指定这个参数。
- `header`：指定作为列名的行。默认为 `0`（即第一行）。如果文件中没有列名，可以设置为 `None`。
- `index_col`：指定哪一列用作行索引（标签）。默认情况下，索引是一个整数序列。
- `usecols`：返回DataFrame的一部分列。默认情况下，返回所有列。可以传递列名的列表或使用列位置的整数列表。
- `nrows`：要读取的行数（从文件开始处算起）。这可以用来进行部分文件的读取。
- `skiprows`：需要跳过的行号列表（从0开始），或是一个范围（比如 `2:5` 表示跳过第2行到第4行）。
- `na_values`：将特定值视为 NaN（缺失值）。
- `dtype`：为每列指定数据类型。这可以提高读取性能，尤其是在处理大型文件时。

### 示例

假设你有一个名为 `example.csv` 的文件，内容如下：

```
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
```

你可以使用以下代码来读取这个文件，并设置 `'Name'` 列作为行索引：

```python
import pandas as pd

df = pd.read_csv('example.csv', index_col='Name')

print(df)
```

输出将是：

```
         Age         City
Name                    
Alice     30     New York
Bob       25  Los Angeles
Charlie   35      Chicago
```

通过这种方式，Pandas 提供了一种非常灵活和强大的方式来读取和分析 CSV 文件中的数据。

## .iloc()

`.iloc[]` 是 Pandas 中 DataFrame 和 Series 对象的一个非常有用的属性，它允许你基于整数位置的索引来选择数据。与 `.loc[]`
不同，`.iloc[]` 主要用于基于位置的索引，而不是基于标签的索引。这意味着你可以通过行号和列号（对于 DataFrame）或位置（对于
Series）来访问数据。

### 基本用法

对于 DataFrame，`.iloc[]` 接受一个元组作为索引器，其中第一个元素是行位置，第二个元素是列位置（如果指定了列的话）。位置索引是从
0 开始的。

```python
import pandas as pd

# 创建一个示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 使用 .iloc[] 访问第一行第二列的数据（注意 Python 是从 0 开始计数的）
print(df.iloc[0, 1])  # 输出: 5

# 访问前两行
print(df.iloc[:2])

# 访问第二列和第三列
print(df.iloc[:, 1:3])
```

### 切片

`.iloc[]` 支持切片操作，允许你选择数据的一个子集。切片操作遵循 Python 的切片规则，即 `start:stop:step`，其中 `start`
是起始位置（包含），`stop` 是结束位置（不包含），`step` 是步长（默认为 1）。

```python
# 访问第一行到第二行（不包含第三行），以及第一列到第三列（不包含第四列）
print(df.iloc[0:2, 0:3])

# 每隔一行取数据
print(df.iloc[::2])

# 反转选择数据（从后往前）
print(df.iloc[::-1])
```

### 注意事项

- `.iloc[]` 是基于位置的索引，因此它不接受标签作为索引器。
- 如果 DataFrame 的索引或列名是数字，并且你试图使用这些数字作为 `.loc[]` 的索引器，Pandas
  可能会将它们解释为位置索引而不是标签索引。在这种情况下，使用 `.iloc[]` 可以避免混淆。
- `.iloc[]` 非常适合于当你确切知道你想要访问的数据的位置时。如果你知道数据的标签但不确定它们的位置，那么 `.loc[]`
  可能是更好的选择。

总之，`.iloc[]` 是 Pandas 中一个强大的工具，它允许你基于位置索引来快速访问和修改 DataFrame 或 Series 中的数据。

## to_sql

在 Python 中，特别是在使用 pandas 库进行数据分析时，`to_sql` 方法是一个非常有用的功能，它允许你将 DataFrame（pandas
中的核心数据结构）直接保存到 SQL 数据库中。这个方法通常与 SQLAlchemy 库一起使用，因为 SQLAlchemy 提供了一个高级接口来连接和操作数据库。

下面是如何使用 pandas 的 `to_sql` 方法将 DataFrame 保存到 SQL 数据库的基本步骤：

1. **安装必要的库**：确保你已经安装了 pandas 和 SQLAlchemy，以及用于连接你目标数据库的数据库适配器（如 pymysql 用于
   MySQL，psycopg2 用于 PostgreSQL 等）。

2. **创建数据库引擎**：使用 SQLAlchemy 的 `create_engine` 函数创建一个数据库引擎。这个引擎将用于与数据库进行通信。

3. **准备 DataFrame**：确保你的 pandas DataFrame 已经准备好要保存到数据库中。这可能包括设置适当的列名和数据类型。

4. **使用 `to_sql` 方法**：调用 DataFrame 的 `to_sql` 方法，将 DataFrame
   保存到数据库中。你需要指定表名、数据库引擎，以及其他一些可选参数（如 `if_exists`，用于控制如果表已存在时的行为）。

下面是一个示例，展示了如何将一个 pandas DataFrame 保存到 MySQL 数据库中：

```python
import pandas as pd
from sqlalchemy import create_engine

# 创建一些示例数据
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [24, 27, 22],
        'city': ['New York', 'Paris', 'Berlin']}
df = pd.DataFrame(data)

# 创建数据库引擎（这里以 MySQL 为例，使用 pymysql 驱动）
# 注意：替换下面的用户名、密码、主机、端口和数据库名为你的实际信息
engine = create_engine('mysql+pymysql://username:password@host:port/database_name')

# 将 DataFrame 保存到数据库中的新表
# 如果表已存在，并且你想替换它，可以设置 if_exists='replace'
# 其他选项包括 'fail'（如果表存在则引发错误）和 'append'（在现有表上追加数据）
df.to_sql('people', con=engine, index=False, if_exists='replace')

# 注意：index=False 表示不将 DataFrame 的索引作为一列保存到数据库中
```

在这个示例中，我们首先创建了一个包含一些示例数据的 pandas DataFrame。然后，我们使用 SQLAlchemy 的 `create_engine` 函数创建了一个
MySQL 数据库的引擎。最后，我们调用了 DataFrame 的 `to_sql` 方法，将 DataFrame 保存到了名为 `people`
的新表中（如果表已存在，并且我们设置了 `if_exists='replace'`，则旧表将被替换）。

请注意，根据你的数据库配置和权限，你可能需要调整数据库 URL、用户名、密码等参数。此外，如果你的 DataFrame
包含大量数据，将其保存到数据库可能需要一些时间。

## drop

在Pandas中，`drop`是一个非常常用的方法，用于从DataFrame或Series中删除指定的行或列。这个方法非常灵活，可以通过几个参数来控制删除的具体行为。

### DataFrame.drop()

对于DataFrame，`drop`方法的基本语法如下：

```python
DataFrame.drop(labels=None, axis=0, index=None, columns=None, errors='raise', inplace=False)
```

- `labels`：要删除的行或列的标签（名称）。在较新版本的Pandas中，推荐使用`index`或`columns`参数来明确指定是删除行还是列，尽管`labels`参数仍然可以工作。
- `axis`：指定操作的轴。`0`或`index`表示沿着行的方向操作（即删除行），`1`或`columns`表示沿着列的方向操作（即删除列）。
- `index`：直接指定要删除的行标签的列表或数组。
- `columns`：直接指定要删除的列标签的列表或数组。
- `errors`：指定如果`labels`参数中的标签不在DataFrame中时的处理方式。`'raise'`（默认值）表示引发错误，`'ignore'`表示忽略错误。
- `inplace`：布尔值，指示是否在原DataFrame上进行修改。如果为`True`，则直接在原DataFrame上修改；如果为`False`，则返回一个新的DataFrame对象，原DataFrame保持不变。

### 示例

假设我们有一个DataFrame `df`，如下所示：

```python
import pandas as pd

data = {
    'Name': ['Tom', 'Jerry', 'Mickey'],
    'Age': [5, 7, 8],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
```

#### 删除列

要删除名为`Age`的列，可以使用以下任一方法：

```python
df.drop('Age', axis=1, inplace=True)  # 使用axis参数
# 或者
df.drop(columns=['Age'], inplace=True)  # 使用columns参数，这是更明确的方式
```

#### 删除行

要删除索引为1的行（注意Pandas的索引是从0开始的），可以使用以下任一方法：

```python
df.drop(index=1, inplace=True)  # 使用index参数
# 或者
df.drop(labels=1, inplace=True)  # 使用labels参数（尽管在这种情况下，推荐使用index）
```

注意，在使用`inplace=True`时，原DataFrame `df` 会被直接修改。如果你不想修改原DataFrame，可以省略`inplace=True`参数，并将结果赋值给一个新的DataFrame变量：

```python
df_without_age = df.drop('Age', axis=1)  # df_without_age是删除了'Age'列的新DataFrame，df保持不变
```

## read_sql_query

`read_sql_query` 是 pandas 库中用于从 SQL 数据库读取数据的一个函数，它属于 `pandas.read_sql_query`。这个函数允许你执行一个
SQL 查询，并将查询结果直接作为一个 DataFrame 返回。这对于数据分析和数据科学项目来说非常有用，特别是当你需要从数据库中提取数据进行分析时。

### 基本用法

要使用 `read_sql_query`，你需要先安装 pandas 库（如果还没有安装的话），并且确保你有访问目标数据库的权限和必要的数据库连接信息（如数据库类型、主机名、端口、用户名、密码等）。

以下是一个基本的使用示例：

```python
import pandas as pd
import sqlite3

# 连接到 SQLite 数据库（这里以 SQLite 为例，但可以是任何支持的数据库）
# 注意：这里使用内存中的 SQLite 数据库仅作为示例
conn = sqlite3.connect(':memory:')

# 创建一个示例表并插入一些数据
conn.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')
conn.execute("INSERT INTO stocks VALUES ('2023-01-01','BUY','RHAT',100,35.14)")

# 使用 read_sql_query 读取数据
query = "SELECT * FROM stocks"
df = pd.read_sql_query(query, conn)

print(df)

# 关闭数据库连接
conn.close()
```

### 参数

`read_sql_query` 函数有几个重要的参数：

- `sql`: 要执行的 SQL 查询字符串。
- `con`: SQLAlchemy 引擎或数据库连接对象，用于执行查询。
- `index_col`: 用作 DataFrame 索引的列名或列位置列表。
- `coerce_float`: 尝试将非字符串、非数字对象转换为浮点数。默认为 True。
- `params`: 用于 SQL 查询的参数（以防止 SQL 注入）。这应该是一个字典或元组列表。
- `parse_dates`: 尝试将数据解析为日期。可以是列名的列表、列名的字典或单个列名。
- `chunksize`: 如果指定，则返回一个迭代器，该迭代器每次迭代时都会返回指定大小的块。这对于处理大量数据非常有用。

### 注意事项

- 在使用 `read_sql_query` 时，请确保你的 SQL 查询是安全的，特别是当查询中包含用户输入时。使用参数化查询（通过 `params`
  参数）来避免 SQL 注入攻击。
- 对于大型数据库，考虑使用 `chunksize` 参数来分批加载数据，以避免内存不足的问题。
- 当你完成数据库操作时，不要忘记关闭数据库连接。在上面的示例中，我们使用 `conn.close()` 来关闭 SQLite
  连接。对于其他数据库，关闭连接的方法可能略有不同。

# click

`click` 是 Python
中的一个第三方库，用于创建命令行接口（CLI）。它让开发者能够轻松地为他们的应用程序添加命令行接口，而不需要编写复杂的解析器代码。`click`
提供了许多装饰器和函数，用于定义命令行选项、参数和命令。

### 安装 Click

首先，你需要确保已经安装了 `click`。如果还没有安装，可以通过 pip 来安装：

```bash
pip install click
```

### 基本用法

以下是一个使用 `click` 创建简单命令行工具的示例：

```python
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f'Hello {name}!')


if __name__ == '__main__':
    hello()
```

在这个示例中，我们定义了一个名为 `hello` 的命令，它接受一个 `--count` 选项（默认为 1）和一个位置参数 `name`
。当运行这个程序并传入相应的参数时，它会打印出指定次数的问候语。

### 运行程序

假设上述程序保存在名为 `hello.py` 的文件中，你可以通过以下方式运行它：

```bash
python hello.py John
```

这将输出：

```
Hello John!
```

如果你想要增加问候次数，可以这样做：

```bash
python hello.py --count=3 John
```

输出将是：

```
Hello John!
Hello John!
Hello John!
```

### Click 的优势

- **简单性**：`click` 提供了一个直观的 API 来创建命令行接口，减少了编写自定义解析器的需要。
- **灵活性**：你可以定义任意数量的命令、选项和参数，以及它们之间的复杂关系。
- **自动帮助**：`click` 会自动生成帮助信息，包括命令的描述、选项和参数的说明。
- **嵌套命令**：支持将命令组织成子命令，创建更复杂的命令行接口。

`click` 是 Python 社区中非常流行的命令行工具创建库，它为快速、轻松地创建命令行接口提供了强大的支持。
