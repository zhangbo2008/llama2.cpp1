# llama2.cpp1


2024-01-03,10点14
自己重头搭建,不用docker.看看适配性. 参考这个项目:https://github.com/soulteary/docker-llama2-chat

  1. wget https://github.com/ggerganov/llama.cpp/archive/refs/tags/master-eb542d3.tar.gz
     注意一定是这个版本eb542d3, 因为新版本已经不支持ggml了.会加载模型错误.
     新版本需要gguf格式.这个以后再说.
  2.  
    解压
    cd 刚才解压的文件夹
    mkdir build
    cd build
    cmake ..
    cmake --build . --config Release





  ./build/bin/main -m Chinese-Llama-2-7b.ggmlv3.q8_0.bin -n 256 --repeat_penalty 1.0 --color -i -r "User:" -f prompts/chat-with-bob.txt