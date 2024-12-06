import namemaker
import os
from application_constants import *
import build_name_lists
import random


def build_full_name():
    # check to ensure name lists have been generated
    if (
        not os.path.exists(FIRST_NAME_TXT_NAME)
        or os.path.getsize(FIRST_NAME_TXT_NAME) == 0
    ) or (
        not os.path.exists(LAST_NAME_TXT_NAME)
        or os.path.getsize(LAST_NAME_TXT_NAME) == 0
    ):
        build_name_lists.generate_name_text_files()

    first_name_set = namemaker.make_name_set(FIRST_NAME_TXT_NAME, order=3)
    last_name_set = namemaker.make_name_set(LAST_NAME_TXT_NAME, order=3)

    full_name = (
        first_name_set.make_name(
            exclude_history=True, exclude_real_names=False, add_to_history=True
        ).capitalize()
        + " "
        + last_name_set.make_name(
            exclude_history=True, exclude_real_names=False, add_to_history=True
        ).capitalize()
    )

    return full_name


def build_position():
    return random.choice(BASEBALL_POSITIONS)


def build_number():
    return random.randint(1, 99)


def build_team_name():
    team_name = []

    with open(CITY_NAMES_TXT_NAME) as f:
        lines = f.readlines()
        team_name.append(random.choice(lines)[:-1])

    # only add adjective half the time
    if random.randint(0, 1) == 1:
        with open(ENGLISH_ADJECTIVES_TXT_NAME) as f:
            lines = f.readlines()
            team_name.append(random.choice(lines)[:-1].capitalize())

    with open(ENGLISH_NOUNS_TXT_NAME) as f:
        lines = f.readlines()
        team_name.append(pluralize_word(random.choice(lines)[:-1]).capitalize())

    return " ".join(team_name)


def build_full_player():
    number = build_number()
    position = build_position()
    player_name = build_full_name()
    team_name = build_team_name()

    return f"#{number} {player_name}, {position} for the {team_name}"
