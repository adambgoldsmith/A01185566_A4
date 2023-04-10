"""
Adam Goldsmith
A01185566
"""


def print_intro_lore() -> None:
    """
    Print intro lore
    """
    print(f"\"Captain? Captain! Wake up! Today is your expedition and you're leaving in 5 minutes!\"\n\n"
          f"You open your eyes and look around at the small, cramped cabin of your airship.\n"
          f"Peering out a small window, you see your hometown of Skyport and the bustling harbor.\n"
          f"The clouds cradle skyport, which is slowly drifting through the clear, cobalt atmosphere.\n\n"
          f"Today is the day you've been waiting for.\n"
          f"A chance to find Kiwi, your beloved pet parrot, who was blown away in a recent void storm.\n\n"
          f"You quickly throw on your uniform and run out of the cabin towards the helm of the ship.\n"
          f"With sails at full mast, you gently glide out into the cloudy blue.\n\n"
          f"Your adventure begins here...")


def print_end_lore() -> None:
    """
    Print end lore
    """
    print(f"You hear a distant 'squaw' coming from ahead and instantly recognize what it is.\n"
          f"You see Kiwi, your parrot, circling the void, confused and afraid.\n"
          f"As your airship sails closer, Kiwi flys towards you frantically, before landing on your shoulder.\n"
          f"You've done it captain! You've rescued Kiwi. Congratulations!\n"
          f"With your old friend by your side, you set off once again to your home in Skyport.\n\n"
          f"~THE END~\n\n"
          f"Thanks for playing!")


def get_region(region_number: int) -> list:
    """
    Get current region

    :param region_number: an integer
    :precondition: region_number must be an integer
    :postcondition: gets the player's current region
    :return: list of region information
    """
    if type(region_number) is not int:
        raise TypeError("Region_number must be an integer")
    regions = {
        0: [f"The Cloud Expanse", 
            f"The several thousand clouds here mesmerize you", 
            f"The sun reflects off of the glittering clouds that surround you.",
            f"A flock of seagulls fly overhead, squawking loudly.",
            f"The blue sky is dotted with fluffy white clouds. The view is breathtaking."],
        1: [f"Fogmourne",
            f"There is only fog... As far as the eye can see...", 
            f"You think you hear something slither through the dense fog, but you see nothing.",
            f"The fog seems to have life to it; slowly crawling. Eerily silent.",
            f"The haziness around you has a strange, sinister charm. Mysterious, yet melancholic."], 
        2: [f"The Void Isles", 
            f"Far down below you, large, amethyst crystal spires protrude from the glowing violet sea.", 
            f"You hear the echo of the void calling to you...",
            f"You peer out across the void. It's impossible to tell how big or small this place truly is...",
            f"The lavender sky seems to pulse and shift as you sail through the stale air."],
    }
    return regions[region_number]
