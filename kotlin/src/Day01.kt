fun main() {
    fun part1(input: List<String>): Int {
        var calories = 0
        var maxCalories = 0
        input.forEach {
            if (it.isBlank()) {
                if (calories > maxCalories) {
                    maxCalories = calories
                }
                calories = 0
            } else {
                calories += it.toInt()
            }
        }
        return maxCalories
    }

    fun part2(input: List<String>): Int {
        var calories = 0
        var maxCalories = 0
        var secondMaxCalories = 0
        var thirdMaxCalories = 0
        input.forEachIndexed { index, food ->
            if (food.isBlank() || index == input.lastIndex) {
                if (index == input.lastIndex) {
                    calories = food.toInt()
                }
                if (calories >= maxCalories) {
                    thirdMaxCalories = secondMaxCalories
                    secondMaxCalories = maxCalories
                    maxCalories = calories
                } else if (calories >= secondMaxCalories) {
                    thirdMaxCalories = secondMaxCalories
                    secondMaxCalories = calories
                } else if (calories > thirdMaxCalories) {
                    thirdMaxCalories = calories
                }
                calories = 0
            } else {
                calories += food.toInt()
            }
        }
        return maxCalories + secondMaxCalories + thirdMaxCalories
    }

    val testInput = readInput("Day01_test")
    check(part1(testInput) == 24000)
    check(part2(testInput) == 45000)

    val input = readInput("Day01")
    println(part1(input))
    println(part2(input))
}
