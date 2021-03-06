# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.3](https://github.com/janaSunrise/HypixelIO/releases/tag/v1.2.3) - 11-03-2021

## Added

- Write more docs
- Add more model fields
- Add modular models
- Add ratelimiting features.
- Add more utility methods.
- Add resources endpoints

## [1.2.2](https://github.com/janaSunrise/HypixelIO/releases/tag/v1.2.2) - 11-03-2021

## Added

- A portal for async to sync with threading.

## Fixed

- Fixed documentation.
- Added asyncio locking to preserve the async coroutines running at same time.

## [1.2.1](https://github.com/janaSunrise/HypixelIO/releases/tag/v1.2.1) - 09-03-2021

## Fixed

- The Changelog
- The README
- The documentation looks and content.

## [1.2.0](https://github.com/janaSunrise/HypixelIO/releases/tag/v1.2.0) - 09-03-2021

## Added
- Skyblock models
- Skyblock endpoints
- Added HTML documentation
- More utility functions and support to make it easier and reliable.
- Asynchronous support for discord bot devs and other people to keep it non-blocking.

## Fixed
- Rewrote most of the code base.
- Rewrite of the inline documentation.
- Pass API Key as `API-Key` header so it's secure and follows the standards.
- Refactored the methods to get better support and converted into multiple methods so its cleaner.
- Fixed the tests and the errors / exceptions raised when issues arrive.
- Make the rest of the codebase usable by the endpoint user, if needed. Not compulsary.

## [1.1.1](https://github.com/janaSunrise/HypixelIO/releases/tag/v1.1.1) - 29-12-2020

## Added
- Various skin fetch features.
- More utility functions for public usage

## Fixed
- Invalid data accepted error.
- Data not being cached a lot in memory.
- Better performance and integration.

## [1.1.0](https://github.com/janaSunrise/HypixelIO/releases/tag/v1.1.0) - 24-11-2020

### Added
- Various Examples in the source repo
- Added options for inheriting the the base classes, and add or override features.

### Changes:
- Changes various types
- Improved the internal docstrings
- Removed `constants.py` as a source for the global version
- Added Various caching options, and Changed the `CacheBackend` to a dataclass
- Rewrote each function and directives
- High bug fixes, and fixed security issues

### Removed
- Removed the useless code which took over more space

## [0.0.7](https://github.com/janaSunrise/HypixelIO/releases/tag/v0.0.7) - 13-11-2020

## Changes
- Change `tuple` instances to `typing.Union`
- Link requirements.txt dependencies to `setup.py`
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
