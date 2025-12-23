def crisis_handler(filename, routine=False):
    """
    - Handle archive access during routine operations or crisis situations.
    - open and read file and report whether access is ok or
        triggered by a crisis, and handles common failure.
    """
    try:
        if routine:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")

        with open(filename, "r") as vault:
            print(f"SUCCESS: Archive recovered - ``{vault.read()}``")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, analysis required")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    print("")
    crisis_handler("classified_vault.txt")
    print("")
    crisis_handler("standard_archive.txt", routine=True)
    print("\nAll crisis scenarios handled successfully. Archives secure.")
