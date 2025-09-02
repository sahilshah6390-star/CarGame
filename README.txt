Kivy Supercar Massive - Placeholder Project
Owner: Sahil Ohk (@offx.sahil)

Files:
- main.py: Kivy scaffold. Replace assets for full game.
- supercar.kv: UI
- assets/: many car images (total 200), maps, sounds
- data.json: initial save with coins and owned cars

How to run (PC for testing):
1. pip install kivy pillow
2. python main.py

How to build APK:
- Use Buildozer on Linux: install buildozer, edit buildozer.spec to include requirements = python3,kivy,pillow
- Then: buildozer android debug

Notes:
- These are placeholder images/sounds generated programmatically for quick testing.
- Replace assets/*.png and assets/*.ogg with real high-quality sprites and sound effects (Freesound.org or licensed assets).
- The app supports many cars and maps; integrate more gameplay logic into main.py as needed.
