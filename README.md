# 🎮 Catch the Fruits!

A fast-paced 2D arcade game built with **Pygame** that will test your reflexes and precision. Catch as many falling fruits as possible before time runs out!

## ✨ Features

- 🍎 **Dynamic Gameplay** - Fruits fall at increasing speeds as you progress
- ⚡ **Power-ups System** - Freeze time, slow down objects, or earn bonus points
- 🎯 **Collision Detection** - Pixel-perfect collision mechanics
- 🏆 **Score & Leaderboard** - Track your best scores
- 🎨 **Clean UI** - Intuitive menus (main menu, pause, game over)
- 🔧 **Modular Architecture** - Well-organized, maintainable code structure
- ⚙️ **State Management** - Smooth transitions between game states

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Pygame

### Installation

```bash
# Clone the repository
git clone https://github.com/Ericchhun67/CatchingFruits.git
cd CatchingFruits

# Install dependencies
pip install pygame

# Run the game
python main.py
```

## 🎮 How to Play

- **Move**: Use LEFT and RIGHT arrow keys (or A/D) to move your basket
- **Catch**: Collect falling fruits to increase your score
- **Avoid**: Missing fruits ends your game
- **Power-ups**: Grab special items for temporary bonuses:
  - ❄️ Freeze Time - Pause falling objects
  - 🐢 Slow Motion - Reduce falling speed
  - ⭐ Bonus Points - Extra score boost

## 🏗️ Project Structure

```
CatchingFruits/
├── main.py              # Game entry point
├── game_manager.py      # Game state & scoring system
├── player.py            # Player controls & collision
├── object.py            # Fruit spawning & gravity
├── powerup.py           # Power-up effects & mechanics
├── main_menu.py         # Main menu interface
├── pause_menu.py        # Pause menu
├── game_over.py         # Game over screen
└── assets/              # Game sprites & sounds
```

## 🎓 Learning Outcomes

This project demonstrates key game development concepts:

- **Object-Oriented Programming** - Clean class-based architecture
- **Collision Detection** - Accurate hit detection mechanics
- **Game State Management** - Menu systems and game flow control
- **Physics Simulation** - Gravity and velocity calculations
- **Event Handling** - Responsive keyboard input
- **Sprite Management** - Efficient object rendering

## 📸 Screenshots

![Gameplay Screenshot 1](https://github.com/user-attachments/assets/82c1a590-bb5c-476a-8924-0d18fec18a32)
*Catch fruits at increasing speeds*

![Gameplay Screenshot 2](https://github.com/user-attachments/assets/f0102f72-06f2-4890-a405-ddec4b7aceba)
*Use power-ups strategically*

![Game Over Screen](https://github.com/user-attachments/assets/1ab82fa8-567b-4c51-a527-0906d6c726cd)
*Track your high scores*

## 🛠️ Technologies

- **Python 3.8+**
- **Pygame 2.0+**
- **Object-Oriented Design**

## 🎯 Future Enhancements

- [ ] Sound effects and background music
- [ ] Difficulty levels (Easy, Normal, Hard)
- [ ] Multiplayer mode
- [ ] Mobile touch controls
- [ ] Save/load game progress
- [ ] Custom themes and skins
- [ ] Leaderboard with persistent storage

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙌 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Contact & Support

Have questions or feedback? Feel free to open an issue or reach out!

---

**Made with ❤️ by [Ericchhun67](https://github.com/Ericchhun67)** | [⭐ Star this repo!](https://github.com/Ericchhun67/CatchingFruits)
