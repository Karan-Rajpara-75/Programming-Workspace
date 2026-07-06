#include <stdio.h>

// Function to check if year is a leap year
int isLeapYear(int year) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
        return 1;
    else
        return 0;
}

// Zeller’s Congruence formula to find day of week
// 0 = Saturday, 1 = Sunday, 2 = Monday, ...
const char* getDayOfWeek(int d, int m, int y) {
    static const char *days[] = {
        "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
    };

    if (m < 3) {
        m += 12;
        y -= 1;
    }

    int k = y % 100;
    int j = y / 100;
    int dayIndex = (d + (13 * (m + 1)) / 5 + k + (k / 4) + (j / 4) + (5 * j)) % 7;
    return days[dayIndex];
}

int main() {
    int day, month, year;
    printf("Enter your birthdate (DD MM YYYY): ");
    scanf("%d %d %d", &day, &month, &year);

    // Show leap year info
    if (isLeapYear(year))
        printf("✅ %d is a Leap Year.\n", year);
    else
        printf("❌ %d is not a Leap Year.\n", year);

 // Show day of the week
    printf("You were born on a %s.\n", getDayOfWeek(day, month, year));

    return 0;
}