查询 SQL 语句的结构是：`SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT ... OFFSET ...`

写 SQL 的时候需要按照如下顺序写：FROM,WHERE,GROUP BY,HAVING,SELECT,ORDER BY,LIMIT

聚集函数：COUNT(), SUM(), MAX(), MIN(), AVG(), GROUP_CONCAT()

登录 mysql `mysql -u root -p`

查看所有的库 `show databases;`

增加库 `create database db1;` #增加一个叫 db1 的库

查看所有的库 `show databases;`

删除库 `drop database db1;`

查看当前在哪个库 `select database();`

如何选择数据库 `use db1;`

看一下库的结构信息 `show create database db1;`

# SQL 语句执行顺序

在 SQL 中，虽然我们在编写查询时按照`SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT ... OFFSET ...`这样的顺序来组织语句，但实际上，数据库管理系统（DBMS）在执行这些查询时遵循一个不同的逻辑顺序。这个顺序对于理解查询如何被优化和执行是非常重要的。下面是 SQL 查询执行的逻辑顺序（注意，这并不意味着这是物理执行的顺序，因为数据库优化器会尝试以最高效的方式执行查询）：

1. **FROM**：首先，DBMS 会处理`FROM`子句，确定要从哪些表中检索数据。如果查询中包含了连接（JOINs），那么连接操作也会在这个阶段进行。

2. **WHERE**：接下来，DBMS 会应用`WHERE`子句中的条件来过滤`FROM`子句产生的结果集。这一步会排除不满足条件的行。

3. **GROUP BY**：如果查询中包含了`GROUP BY`子句，DBMS 会将结果集中的行分组。分组是基于`GROUP BY`子句中指定的列进行的。分组后，每个组将作为一个单独的记录来处理。

4. **HAVING**：`HAVING`子句用于过滤`GROUP BY`产生的分组。与`WHERE`子句不同，`HAVING`子句是在分组之后应用的，并且它允许使用聚合函数（如`COUNT()`, `SUM()`, `AVG()`等）作为过滤条件。

5. **SELECT**：在这个阶段，DBMS 会根据`SELECT`子句中的列和表达式来选择数据。如果查询中包含了聚合函数，那么这些函数会在此时被计算。

6. **DISTINCT**：如果`SELECT`子句中有`DISTINCT`关键字，DBMS 会去除结果集中的重复行。注意，`DISTINCT`是在`SELECT`之后应用的，但在`ORDER BY`之前。

7. **ORDER BY**：接下来，DBMS 会根据`ORDER BY`子句中的列对结果集进行排序。如果没有指定`ORDER BY`，则结果集的顺序是不确定的。

8. **LIMIT** 和 **OFFSET**：最后，如果查询中包含了`LIMIT`和/或`OFFSET`子句，DBMS 会限制返回的记录数，并可能跳过一定数量的记录。这通常用于分页显示结果。

需要注意的是，虽然上述顺序是逻辑上的，但实际的物理执行顺序可能会因为数据库优化器的决策而有所不同。优化器会尝试以最高效的方式执行查询，这可能会改变操作的物理执行顺序。例如，它可能会决定先执行`JOIN`操作的一部分，然后再应用`WHERE`条件，或者它可能会决定使用索引来加速查询的某些部分。

# 创建数据库

在 SQL 中，`CREATE DATABASE`语句用于创建一个新的数据库。这个语句的基本语法相对简单，但具体细节可能会根据你所使用的数据库管理系统（DBMS）有所不同。以下是一个通用的`CREATE DATABASE`语句的示例：

```sql
CREATE DATABASE database_name;
```

在这里，`database_name`是你想要创建的数据库的名称。这个名称必须唯一，并且遵循你所使用的 DBMS 的命名规则。

### 示例

假设你正在使用 MySQL 或 MariaDB，并且想要创建一个名为`my_new_database`的数据库，你可以使用以下 SQL 语句：

```sql
CREATE DATABASE my_new_database;
```

执行这条语句后，你应该能够在你的 DBMS 中看到名为`my_new_database`的新数据库。

### 带有选项的 CREATE DATABASE

在某些 DBMS 中，`CREATE DATABASE`语句还允许你指定一些额外的选项，以配置新数据库的行为或属性。然而，这些选项是可选的，并且具体可用哪些选项取决于你所使用的 DBMS。

例如，在 MySQL 中，你可以使用`CHARACTER SET`和`COLLATE`选项来指定数据库的默认字符集和校对规则：

```sql
CREATE DATABASE my_new_database
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

这个示例创建了一个名为`my_new_database`的数据库，它使用`utf8mb4`字符集和`utf8mb4_unicode_ci`校对规则。这有助于确保数据库能够存储更广泛的 Unicode 字符，并且对大小写不敏感的比较和排序。

### 注意事项

- 在执行`CREATE DATABASE`语句之前，请确保你有足够的权限来创建数据库。
- 数据库名称是区分大小写的，但这取决于你的 DBMS 和它的配置。在某些系统中，名称在内部会被转换为小写或大写，而在其他系统中则保持原样。
- 创建数据库后，你可能需要使用`USE`语句来选择该数据库，以便在其中创建表和其他数据库对象。例如，在 MySQL 中，你可以使用`USE my_new_database;`来选择你刚刚创建的数据库。

# 创建数据表

在 SQL 中，创建数据表（Table）是通过`CREATE TABLE`语句来完成的。下面是一个简单的例子，展示了如何创建一个名为`Students`的数据表，该表包含四个字段：`ID`（主键，自动增长），`Name`（姓名），`Age`（年龄）和`Gender`（性别）。

### 示例 SQL 语句

```sql
CREATE TABLE Students (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Gender ENUM('Male', 'Female', 'Other')
);
```

### 说明

- `CREATE TABLE Students`：这告诉数据库要创建一个名为`Students`的新表。
- 括号内的部分定义了表的结构，即表包含哪些字段（列）以及这些字段的数据类型和其他属性。
- `ID INT AUTO_INCREMENT PRIMARY KEY`：定义了一个名为`ID`的字段，其数据类型为整数（`INT`）。`AUTO_INCREMENT`属性表示每当向表中添加新行时，该字段的值会自动增加（前提是它是主键或唯一索引的一部分）。`PRIMARY KEY`约束意味着`ID`字段的每个值都必须是唯一的，并且不允许为`NULL`。
- `Name VARCHAR(100) NOT NULL`：定义了一个名为`Name`的字段，其数据类型是可变长度的字符串（`VARCHAR`），最大长度为 100 个字符。`NOT NULL`约束意味着在创建记录时，该字段不能留空。
- `Age INT`：定义了一个名为`Age`的字段，其数据类型为整数（`INT`），表示学生的年龄。
- `Gender ENUM('Male', 'Female', 'Other')`：定义了一个名为`Gender`的字段，其数据类型为枚举（`ENUM`），只能包含三个预定义值之一：'Male'、'Female'或'Other'。

### 注意

- 不同的数据库系统（如 MySQL、SQL Server、Oracle 等）在语法上可能略有差异。上面的例子是以 MySQL 为例。
- 在某些数据库系统中，可能需要使用不同的机制来实现自增主键，例如在 SQL Server 中，你会使用`IDENTITY`属性而不是`AUTO_INCREMENT`。
- 创建表时，请确保你拥有足够的权限来执行此操作，并且表名在当前数据库中是唯一的。
- 根据实际需要，你可能还会添加其他字段、约束（如外键约束）或索引来优化你的表。

# sql 语句插入数据

-- 假设我们有一个名为 `users` 的表，它有三个字段：`id`，`name` 和 `email`。
-- 以下 SQL 语句向 `users` 表中插入一条新数据：

INSERT INTO users (id, name, email) VALUES (1, '张三', 'zhangsan@example.com');

-- 如果你想插入多条数据，可以这样做：

INSERT INTO users (id, name, email) VALUES
(2, '李四', 'lisi@example.com'),
(3, '王五', 'wangwu@example.com'),
(4, '赵六', 'bobing@example.com');

-- 如果你不确定字段的顺序，也可以省略字段名称，只给值：

INSERT INTO users VALUES (5, '孙七', 'sunqi@example.com');

在这个例子中，我们向 users 表中插入了一条新的记录。如果你的表有更多的字段，你可以在 INSERT INTO 语句中包含它们，只要在 VALUES 后面提供相应的值。如果所有的字段都要插入值，你可以省略 id, name, email 这一部分，直接写 VALUES。

# 聚集函数

## count()

在 SQL 中，当你使用 `COUNT()` 函数时，默认情况下，`COUNT(*)` 会计算包括 NULL 在内的所有行数，而 `COUNT(column_name)` 则会计算指定列中非 NULL 值的数量。如果你想要确保 `COUNT()` 函数不记录 NULL 值，你应该明确指定列名而不是使用 `*`。

### 示例

假设我们有一个名为 `employees` 的表，其中包含 `id`, `name`, 和 `department_id` 等列，其中 `department_id` 列可能包含 NULL 值。

#### 1. 使用 `COUNT(*)` 计算总行数（包括 NULL）

```sql
SELECT COUNT(*) FROM employees;
```

这条语句会返回 `employees` 表中的所有行数，包括 `department_id` 为 NULL 的行。

#### 2. 使用 `COUNT(column_name)` 排除 NULL 值

```sql
SELECT COUNT(department_id) FROM employees;
```

这条语句会返回 `department_id` 列中非 NULL 值的数量，即排除了 `department_id` 为 NULL 的行。

### 结论

如果你希望 `COUNT()` 函数不记录 NULL 值，你应该指定列名而不是使用 `*`。这是处理 NULL 值时常见的需求，特别是当你需要统计非空（非 NULL）数据项的数量时。

### 注意

- 当你使用 `COUNT(DISTINCT column_name)` 时，同样会排除 NULL 值，因为 `DISTINCT` 操作会去除重复值，包括 NULL（在 SQL 中，NULL 被视为特殊的“未知”值，任何与 NULL 的比较操作都会返回 NULL，因此它不会被视为重复值）。
- 在某些情况下，如果表非常大且你主要关心非 NULL 值的数量，使用 `COUNT(column_name)` 可能会比 `COUNT(*)` 更快，因为数据库可能不需要扫描整个列来找到 NULL 值。然而，实际的性能差异取决于数据库的实现和数据的具体情况。
