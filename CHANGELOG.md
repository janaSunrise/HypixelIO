# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.3](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.3) - 23-10-2020

### Added
- The `__repr__` and `__str__` for some methods
- Added `Leaderboard` and `GameCount` Stats
- Added Caching to the requests
- Added Converter of `username_to_uuid`
- Added New exception: `MojangAPIError`

### Changed
- The class variables to global constants
- Stored all the constants in a single unique file
- Converted all the main usage files into a different library package

## [0.0.2](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.2) - 22-10-2020

### Added
- Fix the API Key error
- Fix the API_Error raised on when the `get_key_info()` is utilized.
- Fix the Boosters bug error due to small typos
- Fix the Self argument error, when the function was moved out of the class, to be a utility function.

## Changed
- Change Async and Coroutines and make them Synchronous

## Removed
- Async features


## [0.0.1](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.1) - 21-10-2020

### Added
- Use the Code with multithreading, for Many process tasks.
- Have several Search features.
- Supports valid authentication
- Basic, Important documentations added, Well explained, and better than other libraries.

### Changed
- Change the Code style
- Refactor things
- Remove useless whitespaces
- Change a Typo of `friends.Friend` to `friends.Friends`
