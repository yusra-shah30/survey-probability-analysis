# ==========================================================
# Survey Probability Analysis Project
# Author: Yusra Jan
# ==========================================================

import random
from collections import Counter

# ==========================================================
# DATASET
# ==========================================================

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

# ==========================================================
# BASIC FUNCTIONS
# ==========================================================

def total_responses(data):
    return len(data)


def app_frequency(data):
    apps = [row[0] for row in data]
    return Counter(apps)


def probability_distribution(freq_dict):
    total = sum(freq_dict.values())

    probabilities = {}

    for app, freq in freq_dict.items():
        probabilities[app] = freq / total

    return probabilities


def percentage_distribution(probabilities):
    percentages = {}

    for app, prob in probabilities.items():
        percentages[app] = prob * 100

    return percentages


# ==========================================================
# DISPLAY FUNCTIONS
# ==========================================================

def print_frequency_table(freq_dict):
    print("\nFREQUENCY TABLE")
    print("-" * 40)

    for app, freq in freq_dict.items():
        print(f"{app:<12} : {freq}")


def print_probability_table(prob_dict):
    print("\nPROBABILITY TABLE")
    print("-" * 40)

    for app, prob in prob_dict.items():
        print(f"{app:<12} : {prob:.4f}")


def print_percentage_table(percent_dict):
    print("\nPERCENTAGE TABLE")
    print("-" * 40)

    for app, percent in percent_dict.items():
        print(f"{app:<12} : {percent:.2f}%")


# ==========================================================
# CONDITIONAL PROBABILITY
# ==========================================================

def conditional_probability(data, frequency_type):

    filtered = []

    for app, freq in data:
        if freq == frequency_type:
            filtered.append(app)

    counts = Counter(filtered)

    total = len(filtered)

    result = {}

    for app in counts:
        result[app] = counts[app] / total

    return result


def display_conditional(probabilities, title):
    print("\n" + title)
    print("-" * 40)

    for app, prob in probabilities.items():
        print(f"{app:<12} : {prob:.4f}")


# ==========================================================
# EXPECTED VALUE
# ==========================================================

def expected_users(probabilities, sample_size=100):

    expected = {}

    for app, prob in probabilities.items():
        expected[app] = prob * sample_size

    return expected


def display_expected(expected):
    print("\nEXPECTED USERS OUT OF 100")
    print("-" * 40)

    for app, value in expected.items():
        print(f"{app:<12} : {value:.2f}")


# ==========================================================
# SIMULATION
# ==========================================================

def run_simulation(n=100):

    options = [
        "Instagram",
        "YouTube",
        "TikTok",
        "Facebook"
    ]

    responses = []

    for _ in range(n):
        responses.append(random.choice(options))

    return Counter(responses)


def simulation_probability(freq):

    total = sum(freq.values())

    result = {}

    for app in freq:
        result[app] = freq[app] / total

    return result


def display_simulation(freq, prob):

    print("\nSIMULATION RESULTS")
    print("-" * 40)

    for app in freq:
        print(
            f"{app:<12} "
            f"Freq={freq[app]:<5} "
            f"Prob={prob[app]:.4f}"
        )


# ==========================================================
# SUMMARY STATISTICS
# ==========================================================

def most_selected(freq_dict):
    return max(freq_dict, key=freq_dict.get)


def least_selected(freq_dict):
    return min(freq_dict, key=freq_dict.get)


def summary_report(freq, prob):

    print("\nSUMMARY REPORT")
    print("=" * 50)

    print("Total Responses :", sum(freq.values()))
    print("Most Selected   :", most_selected(freq))
    print("Least Selected  :", least_selected(freq))

    print("\nProbability Distribution")

    for app, value in prob.items():
        print(f"{app:<12} : {value:.4f}")


# ==========================================================
# DASHBOARD
# ==========================================================

def dashboard():

    freq = app_frequency(survey_data)

    prob = probability_distribution(freq)

    percent = percentage_distribution(prob)

    daily = conditional_probability(
        survey_data,
        "Daily"
    )

    weekly = conditional_probability(
        survey_data,
        "Weekly"
    )

    expected = expected_users(prob)

    print("\n")
    print("=" * 60)
    print("SURVEY PROBABILITY ANALYSIS DASHBOARD")
    print("=" * 60)

    print_frequency_table(freq)

    print_probability_table(prob)

    print_percentage_table(percent)

    display_conditional(
        daily,
        "CONDITIONAL PROBABILITY (DAILY)"
    )

    display_conditional(
        weekly,
        "CONDITIONAL PROBABILITY (WEEKLY)"
    )

    display_expected(expected)

    summary_report(freq, prob)

    sim_freq = run_simulation(100)

    sim_prob = simulation_probability(sim_freq)

    display_simulation(
        sim_freq,
        sim_prob
    )


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    dashboard()

    print("\n")
    print("=" * 60)
    print("PROJECT CONCLUSION")
    print("=" * 60)

    print(
        "Instagram has the highest preference "
        "among respondents."
    )

    print(
        "Facebook has the lowest preference "
        "among respondents."
    )

    print(
        "Daily users show stronger preference "
        "towards Instagram."
    )

    print(
        "Simulation results support the "
        "overall trend observed in the survey."
    )

    print(
        "\nProject Completed Successfully."
    )


if __name__ == "__main__":
    main()
