// 100 years 
#include <stdio.h>

// Function to check leap year
int isLeapYear(int year) {
    if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
        return 1;
    return 0;
}

// Function to get number of days in a month
int getDaysInMonth(int month, int year) {
    switch (month) {
        case 1: return 31;
        case 2: return (isLeapYear(year) ? 29 : 28);
        case 3: return 31;
        case 4: return 30;
        case 5: return 31;
        case 6: return 30;
        case 7: return 31;
        case 8: return 31;
        case 9: return 30;
        case 10: return 31;
        case 11: return 30;
        case 12: return 31;
        default: return 0;
    }
}

// Function to calculate day of week (0=Sunday, 1=Monday,...)
int getDayOfWeek(int day, int month, int year) {
    int y = year - (month < 3);
    int m = month + (month < 3 ? 12 : 0);
    int d = (y + y/4 - y/100 + y/400 + (31*m)/12 + day) % 7;
 return d;
}

// Function to print a month's calendar
void printMonth(int month, int year, int startDay) {
    const char *months[] = {
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    };
    
    int days = getDaysInMonth(month, year);
    printf("\n\n  ------------%s %d-------------\n", months[month-1], year);
    printf("  Sun  Mon  Tue  Wed  Thu  Fri  Sat\n");

    // Print initial spaces
    for (int i = 0; i < startDay; i++)
        printf("     ");

    // Print days
    for (int d = 1; d <= days; d++) {
        printf("%5d", d);
        if (++startDay > 6) {
            startDay = 0;
            printf("\n");
        }
    }
    printf("\n");
}

// Main function
int main() {
    int startYear;
    printf("Enter the starting year: ");
    scanf("%d", &startYear);
 int day = getDayOfWeek(1, 1, startYear); // Day of week for Jan 1 of startYear

    for (int year = startYear; year < startYear + 100; year++) {
        for (int month = 1; month <= 12; month++) {
            printMonth(month, year, day);
            day = (day + getDaysInMonth(month, year)) % 7; // Update for next month
        }
    }
    return 0;
}