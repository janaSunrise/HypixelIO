# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.7](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.7) - 13-11-2020

## Changes
- Change `tuple` instances to `typing.Union`
- Shift requirements.txt dependencies to `setup.py`
- Remove all the build files of the dependencies, and documentations.

## [0.0.6](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.6) - 13-11-2020

### Added
- Added attributes like `__author__` and `__version__`
- Added Manifest
- Added support for Comparisons like
    - `obj1 == obj2`
    - `obj1 > obj2`
    - `obj1 >= obj2`

## [0.0.5](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.5) - 04-11-2020

### Added
- Modular caching of requests,
- Added timeout for the cache and fetch
- Allow users to specify the caching according to needs, and various functions to make experience better
- Functions allowed:
    - Clearing Cache
    - Uninstall cache, If enabled
    - removing expired cache
    - Get the existsing cache, and check it.

## [0.0.4](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.4) - 31-10-2020

### Added
- The `__repr__` and `__str__` for some methods
- Added `find_guild` to the client functions
- New model: `FindGuild` containing the ID during finding.
- Added Converter of `uuid_to_username`

### Changed
- Fix The `__repr__` and `__str__` for some classes
- Converted all the main usage files into a different library package again
- Split and cleaned the things.

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
