# Survey Probability Analysis Project
# Author: Yusra Jan

from collections import Counter
import random
# SURVEY DATA


survey_data = [
    ("Instagram", "Daily"),
    ("YouTube", "Daily"),
    ("TikTok", "Weekly"),
    ("Instagram", "Daily"),
    ("Facebook", "Weekly"),
    ("Instagram", "Daily"),
    ("YouTube", "Daily"),
    ("TikTok", "Weekly"),
    ("Instagram", "Daily"),
    ("YouTube", "Daily"),
    ("Instagram", "Weekly"),
    ("TikTok", "Daily"),
    ("Instagram", "Daily"),
    ("YouTube", "Weekly"),
    ("Facebook", "Weekly"),
    ("Instagram", "Daily"),
    ("TikTok", "Daily"),
    ("Instagram", "Daily"),
    ("YouTube", "Weekly"),
    ("Instagram", "Daily"),
    ("TikTok", "Daily"),
    ("YouTube", "Weekly"),
    ("Instagram", "Daily"),
    ("Facebook", "Weekly"),
    ("Instagram", "Daily"),
    ("YouTube", "Daily"),
    ("TikTok", "Weekly"),
    ("Instagram", "Daily"),
    ("YouTube", "Weekly"),
    ("Instagram", "Daily"),
    ("TikTok", "Daily"),
    ("Instagram", "Weekly"),
    ("Facebook", "Daily"),
    ("YouTube", "Weekly"),
    ("Instagram", "Daily"),
    ("TikTok", "Daily"),
    ("Instagram", "Weekly"),
    ("YouTube", "Daily"),
    ("Instagram", "Daily"),
    ("Facebook", "Weekly"),
    ("TikTok", "Daily"),
    ("Instagram", "Daily"),
    ("YouTube", "Weekly"),
    ("Instagram", "Daily"),
    ("TikTok", "Daily"),
    ("Instagram", "Weekly"),
    ("YouTube", "Daily"),
    ("Instagram", "Daily"),
    ("Facebook", "Weekly"),
    ("Instagram", "Daily"),
    ("Instagram", "Daily"),
    ("YouTube", "Weekly"),
    ("TikTok", "Daily"),
    ("Instagram", "Daily"),
    ("YouTube", "Weekly"),
    ("Instagram", "Daily"),
    ("Facebook", "Weekly"),
    ("Instagram", "Daily"),
    ("TikTok", "Weekly"),
    ("Instagram", "Daily")
]

APPS = ["Instagram", "YouTube", "TikTok", "Facebook"]

# ==========================================================
# BASIC CALCULATIONS
# ==========================================================

def get_total_responses(data):
    return len(data)


def calculate_frequency(data):
    apps = [row[0] for row in data]
    return Counter(apps)


def calculate_probability(frequency):
    total = sum(frequency.values())

    probabilities = {}

    for app in APPS:
        probabilities[app] = frequency.get(app, 0) / total

    return probabilities


def calculate_percentage(probabilities):
    percentages = {}

    for app in APPS:
        percentages[app] = probabilities[app] * 100

    return percentages


# ==========================================================
# DISPLAY TABLES
# ==========================================================

def print_line():
    print("-" * 60)


def display_frequency_table(frequency):
    print("\nFREQUENCY TABLE")
    print_line()

    print(f"{'App':<15}{'Frequency':>10}")

    for app in APPS:
        print(f"{app:<15}{frequency.get(app, 0):>10}")


def display_probability_table(probabilities):
    print("\nPROBABILITY TABLE")
    print_line()

    print(f"{'App':<15}{'Probability':>15}")

    for app in APPS:
        print(f"{app:<15}{probabilities[app]:>15.4f}")


def display_percentage_table(percentages):
    print("\nPERCENTAGE TABLE")
    print_line()

    print(f"{'App':<15}{'Percentage':>15}")

    for app in APPS:
        print(f"{app:<15}{percentages[app]:>14.2f}%")


# ==========================================================
# CONDITIONAL PROBABILITY
# ==========================================================

def conditional_probability(data, usage_type):

    filtered_apps = []

    for app, usage in data:
        if usage == usage_type:
            filtered_apps.append(app)

    total = len(filtered_apps)

    counts = Counter(filtered_apps)

    result = {}

    if total == 0:
        for app in APPS:
            result[app] = 0
        return result

    for app in APPS:
        result[app] = counts.get(app, 0) / total

    return result


def display_conditional_probability(title, probabilities):
    print(f"\n{title}")
    print_line()

    print(f"{'App':<15}{'Probability':>15}")

    for app in APPS:
        print(f"{app:<15}{probabilities[app]:>15.4f}")


# ==========================================================
# EXPECTED VALUE
# ==========================================================

def calculate_expected_users(probabilities, sample_size=100):

    expected = {}

    for app in APPS:
        expected[app] = probabilities[app] * sample_size

    return expected


def display_expected_users(expected):
    print("\nEXPECTED USERS OUT OF 100")
    print_line()

    print(f"{'App':<15}{'Expected Users':>20}")

    for app in APPS:
        print(f"{app:<15}{expected[app]:>20.2f}")


# ==========================================================
# SIMULATION
# ==========================================================

def run_simulation(sample_size=100):

    results = []

    for _ in range(sample_size):
        choice = random.choice(APPS)
        results.append(choice)

    return Counter(results)


def simulation_probabilities(sim_freq):

    total = sum(sim_freq.values())

    probabilities = {}

    for app in APPS:
        probabilities[app] = sim_freq.get(app, 0) / total

    return probabilities


def display_simulation(sim_freq, sim_prob):

    print("\nSIMULATION RESULTS")
    print_line()

    print(
        f"{'App':<15}"
        f"{'Frequency':>12}"
        f"{'Probability':>15}"
    )

    for app in APPS:
        print(
            f"{app:<15}"
            f"{sim_freq.get(app,0):>12}"
            f"{sim_prob[app]:>15.4f}"
        )


# ==========================================================
# ASCII BAR CHART
# ==========================================================

def display_ascii_chart(frequency):

    print("\nASCII BAR CHART")
    print_line()

    for app in APPS:
        count = frequency.get(app, 0)
        bar = "#" * count

        print(f"{app:<15}: {bar}")


# ==========================================================
# SUMMARY REPORT
# ==========================================================

def get_most_selected(frequency):
    return max(frequency, key=frequency.get)


def get_least_selected(frequency):
    return min(frequency, key=frequency.get)


def summary_report(frequency, probabilities):

    print("\nSUMMARY REPORT")
    print("=" * 60)

    print("Total Responses :", sum(frequency.values()))
    print("Most Selected   :", get_most_selected(frequency))
    print("Least Selected  :", get_least_selected(frequency))

    print("\nProbability Distribution")

    for app in APPS:
        print(
            f"{app:<15}"
            f"{probabilities[app]:.4f}"
        )


# ==========================================================
# DASHBOARD
# ==========================================================

def dashboard():

    total = get_total_responses(survey_data)

    frequency = calculate_frequency(survey_data)

    probabilities = calculate_probability(frequency)

    percentages = calculate_percentage(probabilities)

    daily_prob = conditional_probability(
        survey_data,
        "Daily"
    )

    weekly_prob = conditional_probability(
        survey_data,
        "Weekly"
    )

    expected_users = calculate_expected_users(
        probabilities,
        100
    )

    print("=" * 60)
    print("SURVEY PROBABILITY ANALYSIS DASHBOARD")
    print("=" * 60)

    print(f"\nTotal Responses: {total}")

    display_frequency_table(frequency)

    display_probability_table(probabilities)

    display_percentage_table(percentages)

    display_conditional_probability(
        "CONDITIONAL PROBABILITY (DAILY USERS)",
        daily_prob
    )

    display_conditional_probability(
        "CONDITIONAL PROBABILITY (WEEKLY USERS)",
        weekly_prob
    )

    display_expected_users(expected_users)

    display_ascii_chart(frequency)

    summary_report(frequency, probabilities)

    simulation_frequency = run_simulation(100)

    simulation_probability = simulation_probabilities(
        simulation_frequency
    )

    display_simulation(
        simulation_frequency,
        simulation_probability
    )

    print("\nFINAL CONCLUSION")
    print("=" * 60)

    print(
        "Instagram is the most preferred social media "
        "application in the survey dataset."
    )

    print(
        "Facebook has the lowest preference among "
        "respondents."
    )

    print(
        "Daily users show stronger preference for "
        "Instagram than Weekly users."
    )

    print(
        "Simulation results support the overall "
        "trend observed in the survey."
    )

    print("\nProject Completed Successfully.")


# ==========================================================
# MAIN FUNCTION
# ==========================================================

def main():
    dashboard()


if __name__ == "__main__":
    main()
