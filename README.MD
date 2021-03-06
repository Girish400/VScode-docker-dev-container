Issue Type: **Bug**

Version: 1.60.0 (user setup)
Commit: e7d7e9a9348e6a8cc8c03f877d39cb72e5dfb1ff
Date: 2021-09-01T10:41:52.311Z
Electron: 13.1.8
Chrome: 91.0.4472.164
Node.js: 14.16.0
V8: 9.1.269.39-electron.0
OS: Windows_NT x64 10.0.19042

**Steps to Reproduce:**

- Open new terminal from menu, powerlevel10k prompt will work and alias cls will clear the screen. Powerlevel10k prompt and alias cls work as expected. [Image](https://github.com/Girish400/VScode-docker-dev-container/raw/1b08c0130b717d5c00f8dc228095672f82fa8fab/Images/Pk10working.png)

- Run python program using **Run Python file in terminal**,  powerlevel10k prompt will not work and alias cls will not work. [Image](https://github.com/Girish400/VScode-docker-dev-container/raw/1b08c0130b717d5c00f8dc228095672f82fa8fab/Images/Pk10notworking.png)

- But after running the python program, type in **zsh**  in the terminal, powerlevel10k prompt and alias cls will start working [Image](https://github.com/Girish400/VScode-docker-dev-container/raw/master/Images/Pk10workingafterzsh.png)

**Expected result:**
- **Run Python file in terminal** should load the **.zshrc** file and powerlevel10k prompt and alias cls should work without typing zsh in terminal
-  [Github Link to docker file with extension](https://github.com/Girish400/VScode-docker-dev-container)

[Github issue #](https://github.com/microsoft/vscode/issues/132952)