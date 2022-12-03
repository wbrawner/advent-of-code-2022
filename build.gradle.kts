import java.net.URL
import java.net.HttpURLConnection

plugins {
    kotlin("jvm") version "1.7.22"
}

repositories {
    mavenCentral()
}

tasks {
    sourceSets {
        main {
            java.srcDirs("src")
        }
    }

    wrapper {
        gradleVersion = "7.6"
    }
}

tasks.register("downloadInput") {
    doLast {
        val day: String = findProperty("day") as? String ?: error("day is required")
        val challengeUrl = "https://adventofcode.com/2022/day/$day"
        val inputUrl = "$challengeUrl/input"
        exec {
            commandLine("xdg-open", challengeUrl)
        }
        var sessionCookie = System.getenv("AOC_SESSION")
        if (sessionCookie.isNullOrBlank()) {
            error("AOC_SESSION environment variable missing or empty")
        }
        if (!sessionCookie.startsWith("session=")) {
            sessionCookie = "session=$sessionCookie"
        }
        val url = URL(inputUrl)
        val connection = url.openConnection() as HttpURLConnection
        connection.requestMethod = "GET"
        connection.setRequestProperty("Cookie", sessionCookie)
        val content = connection.inputStream.bufferedReader().readText()
        val dayFileName = "Day${day.padStart(2, '0')}"
        File("src", "${dayFileName}_test.txt").createNewFile()
        File("src", "$dayFileName.txt").writeText(content)
        val sourceFile = File("src", "$dayFileName.kt")
        if (sourceFile.exists()) {
            return@doLast
        }
        sourceFile.writeText("""
            fun main() {
                fun part1(input: List<String>): Int {
                    return 0
                }

                fun part2(input: List<String>): Int {
                    return 0
                }

                val testInput = readInput("${dayFileName}_test")
                check(part1(testInput) == 0)
                check(part2(testInput) == 0)

                val input = readInput("$dayFileName")
                println(part1(input))
                println(part2(input))
            }
        """.trimIndent())
    }
}