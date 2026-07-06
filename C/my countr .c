#include <stdio.h>
#include <time.h>

void show_time(const char *country, int offset_hours) {
    time_t rawtime;
    struct tm *timeinfo;

    // Get current UTC time
    time(&rawtime);
    timeinfo = gmtime(&rawtime);

    // Adjust time by offset
    timeinfo->tm_hour += offset_hours;
    mktime(timeinfo);  // Normalize time structure

    printf("%-20s : %02d:%02d:%02d\n", country,
           timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec);
}

int main() {
    printf("Current Time in Major Countries:\n");
    printf("--------------------------------\n");

    show_time("India (IST)", 5 + 30/60);         // UTC +5:30
    show_time("United Kingdom (GMT)", 0);        // UTC +0
    show_time("USA (New York - EST)", -5);       // UTC -5
    show_time("Japan (JST)", 9);                 // UTC +9
    show_time("China (CST)", 8);                 // UTC +8
    show_time("Australia (Sydney)", 10);         // UTC +10
    show_time("Russia (Moscow)", 3);             // UTC +3
    show_time("UAE (Dubai)", 4);                 // UTC +4
    show_time("Brazil (Brasilia)", -3);          // UTC -3
    show_time("South Africa", 2);                // UTC +2

    return 0;
}