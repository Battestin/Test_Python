# TestPython
Instala o Git

Botão direito > Open Git Bash Here #na pasta que quer mandar pro repositório
ou
ir direto pelo VSCode

#inicia o git
git init 

#configura a conta
  #email
  git config --global user.email "you@example.com"
  
  #usuário
  git config --global user.name "Your Name"

#conecta ao repositório online do GitHub
git remote add origin "link do repositório"

#para projetos novos
  #conecta a branch master local com a branch master remoto
  git push --set-upstream origin master

#para projetos ja existentes
  #clona o repositório existente
  git clone https://github.com/fulano/meu-projeto.git
  cd meu-projeto
  

#verifica o status dos arquivos da pasta atual
git status 

#adiciona um arquivo específico. precisa colocar a extensão do arquivo se tiver
git add "Nome do arquivo" 

#adiciona todos os arquivos da pasta
git add . 

#commita uma versão no repositório local
git commit -m "Comentário do commit"

#lista o histórico de commits
git log

#recupera todos os arquivos do commit especificado
git checkout id-do-commit-antigo

#recupera apenas o arquivo específico do commit especificado
git checkout id-do-commit-antigo -- main.py

#recupera apenas o arquivo específico do commit especificado
git restore --source=id-do-commit-antigo main.py

#cria uma branch (linha do tempo alternativa)
git checkout -b nova-branch

#lista as branchs do projeto
git branch

#navega para a branch especificada
git checkout nova-branch

#navega para a branch master (a principal)
git checkout master

#juntas a branch atual a branch especificada (neste caso estamos na master)
git merge nova-branch

#deleta uma branch
git branch -d nova-branch


