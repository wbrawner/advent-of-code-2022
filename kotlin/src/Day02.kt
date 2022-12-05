import java.lang.IllegalArgumentException

fun main() {
    fun part1(input: List<String>): Int {
        var total = 0
        input.forEach { line ->
            val (opponent, me) = line.split(" ").map { it.toMove() }
            val winLossAdjustment = if (opponent beats me) {
                0
            } else if (me == opponent) {
                3
            } else {
                6
            }
            total += winLossAdjustment + me.ordinal + 1
        }
        return total
    }

    fun part2(input: List<String>): Int {
        var total = 0
        input.forEach { line ->
            val (first, second) = line.split(" ")
            val opponent = first.toMove()
            val strategy = second.toStrategy()
            val me = when(strategy) {
                Strategy.LOSE -> opponent.win()
                Strategy.TIE -> opponent.tie()
                Strategy.WIN -> opponent.lose()
            }
            total += (strategy.ordinal * 3) + me.ordinal + 1
        }
        return total
    }

    val testInput = readInput("Day02_test")
    check(part1(testInput) == 15)
    check(part2(testInput) == 12)

    val input = readInput("Day02")
    println(part1(input))
    println(part2(input))
}

enum class Moves {
    ROCK {
        override fun beats(other: Moves): Boolean = other == SCISSORS
        override fun win(): Moves = SCISSORS
        override fun lose(): Moves = PAPER
    },
    PAPER {
        override fun beats(other: Moves): Boolean = other == ROCK
        override fun win(): Moves = ROCK
        override fun lose(): Moves = SCISSORS
    },
    SCISSORS {
        override fun beats(other: Moves): Boolean = other == PAPER
        override fun win(): Moves = PAPER
        override fun lose(): Moves = ROCK
    };

    /**
     * Check whether this move would beat the other move
     */
    abstract infix fun beats(other: Moves): Boolean

    /**
     * Return the move that this move would win against
     */
    abstract fun win(): Moves

    /**
     * Return the move this move would tie with
     */
    fun tie(): Moves = this

    /**
     * Return the move this move would lose against
     */
    abstract fun lose(): Moves
}

enum class Strategy {
    LOSE,
    TIE,
    WIN,
}

fun String.toStrategy() = when (this) {
    "X" -> Strategy.LOSE
    "Y" -> Strategy.TIE
    "Z" -> Strategy.WIN
    else -> throw IllegalArgumentException("Invalid strategy: $this")
}

fun String.toMove(): Moves = when (this) {
    "A", "X" -> Moves.ROCK
    "B", "Y" -> Moves.PAPER
    "C", "Z" -> Moves.SCISSORS
    else -> throw IllegalArgumentException("Invalid move: $this")
}

