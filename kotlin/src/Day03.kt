fun main() {
    fun part1(input: List<String>): Int {
        var priority = 0
        input.forEach { ruckSack ->
            val compartment1 = ruckSack.slice(0 until ruckSack.length / 2).toSet()
            val compartment2 = ruckSack.slice(ruckSack.length / 2 until ruckSack.length).toSet()
            var duplicate: Char? = null
            for (item in compartment1) {
                if (compartment2.contains(item)) {
                    duplicate = item
                    break
                }
            }
            duplicate?.let {
                priority += it.priority()
            }?: throw IllegalStateException("No duplicates found in rucksacks")
        }
        return priority
    }

    fun part2(input: List<String>): Int {
        var priority = 0
        val group = mutableListOf<Set<Char>>()
        input.forEach { ruckSack ->
            group.add(ruckSack.toSet())
            if (group.size != 3) {
                return@forEach
            }
            for (item in group.first()) {
                if (group[1].contains(item) && group[2].contains(item)) {
                    priority += item.priority()
                    break
                }
            }
            group.clear()
        }
        return priority
    }

    val testInput = readInput("Day03_test")
    check(part1(testInput) == 157)
    check(part2(testInput) == 70)

    val input = readInput("Day03")
    println(part1(input))
    println(part2(input))
}

fun Char.priority(): Int = when(code) {
    in 65..90 -> code - 38
    in 97..122 -> code - 96
    else -> throw IllegalArgumentException("Invalid item")
}
