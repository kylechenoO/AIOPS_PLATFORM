# AIOPS PLATFORM 贡献指南

## Git 操作流程

**准备工作**

1. fork项目

2. 把fork后的项目(也就是你自己github名下的仓库)`clone`到本地

3. 在命令行运行 `git branch dev`来创建一个新分支，分支名是`dev`，你也可以用其它任何自己命名的名字

4. 运行 `git checkout dev` 来切换到新分支

5. 添加本项目的远端库，命名为`upstream`（也可以是其他名字），用来获取更新。

   * 在文档库的目录内，运行`git remote add upstream https://github.com/aiops-project/AIOPS_PLATFORM.git` 把本项目文档库添加为远端库

以上步骤是一个初始化流程，只需要做一遍就行，之后请一直在`temp`（或其他名字）分支进行修改。

**每次提交或review前**

6. 在本地目录内，运行`git remote update`更新
7. 在本地目录内，运行`git fetch upstream master`拉取更新到本地 
8. 在本地目录内，使用`git checkout dev`切换回你的日常分支后，运行 `git rebase upstream/master`将更新合并到你的分支

> 如果修改过程中我们的仓库有了更新，在对应的库目录下重复6、7、8步即可。 也可以简写为`git pull --rebase upstream master` 一条命令。或者你用SourceTree等GUI的话，在`push`面板下勾选用变基替代合并。也可以起到相同的作用，巧用变基，可以避免不必要的合并。

9. 修改之后，首先 Push 到你的库，然后登录 GitHub，在你的库的首页可以看到一个 pull request 按钮，点击它，填写一些说明信息，然后提交即可。

参与项目的流程如下

**参与流程**：认领需求 → 开发 → 建Pull Request（简称PR） / 直接提交 → 等待官方合并或其他评论

