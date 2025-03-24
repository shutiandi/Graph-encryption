# Graph-encryption
Research on absolute security encryption technology,
Graph-encryption 
Image encryption technology is a technique and method that encrypts data based on the invariant rules of all basic data in graphic pixels and also incorporates user-defined rules. 
 
In essence, it achieves encryption by continuously transforming file data. The encryption result is reversible, and the key is a regular tile file composed of basic files generated according to custom rules. 
 
Currently, the complete data of the basic tile without modifying the underlying rules in image encryption technology is 172KB (4096*4096). After one - time data dispersion, it has not been tested but does exist. After two - time data dispersion, a color - changing tile file of 4*(2048*2048) can be obtained. After three - time data dispersion, it remains untested, and after n - time data dispersion, it is also untested. The standard theoretical maximum value of n is 4096. After extending the standard, modifying the content of one 4096 low - modulus tile file can trigger a change magnitude of 4096*4096*tile row - column data. The security of non - standard tile file encryption makes decryption a luxury. Theoretically, with infinite subdivision, recombination, and superposition of multiple data tile files, the encryption ability can reach an unimaginable and endless level. 

上手指南

环境设置

克隆仓库:

bash

复制

git clone https://github.com/shutiandi/Graph-encryption.git
 
开发架构
当前项目采用Python作为主要开发语言，目前暂无其他架构的开发计划。

版权说明
本项目采用MIT授权许可。详细的许可信息请参见LICENSE文件。

贡献指南
我们欢迎各种形式的贡献。如果您有兴趣贡献代码，请阅读我们的贡献指南。

致谢
感谢所有为该项目做出贡献的人，包括但不限于代码贡献者、文档编写者和问题报告者。

联系信息
如有任何问题，请通过email 与我们联系。
