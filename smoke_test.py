"""Smoke test: verify all modules import and basic config loads."""


def main() -> int:
    errors: list[str] = []

    try:
        import httpx  # noqa: F401
        import pydantic  # noqa: F401
        import dotenv  # noqa: F401
    except Exception as e:
        errors.append(f"dependency import failed: {e}")

    try:
        import settlebridge_demo  # noqa: F401
        assert settlebridge_demo.__version__ == "0.1.0"
    except Exception as e:
        errors.append(f"package import failed: {e}")

    try:
        from settlebridge_demo.config import Settings
        s = Settings()
        assert s.log_level in ("DEBUG", "INFO", "WARNING", "ERROR")
    except Exception as e:
        errors.append(f"config load failed: {e}")

    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        return 1

    print("settlebridge-demo smoke test: ALL OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
