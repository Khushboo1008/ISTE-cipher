const fs = require('fs')
const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
const generateRandomString = (n) =>{
    let result = ' ';
    const charactersLength = characters.length;
    for ( let i = 0; i < n; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    return result;
}
const createFolders = (n) => {
    for(let i = 0; i < n; i++) {
        fs.mkdirSync(`./Dummy/${generateRandomString(10)}`)
    }
    createFiles()
}
const createFiles = () => {
    const dirs = fs.readdirSync('./Dummy','utf-8')
    console.log(dirs)
    dirs.forEach((dir,index)=>{
        fs.writeFileSync(`./Dummy/${dir}/${generateRandomString(10)}.txt`, 'Wrong File Please try again')
    })
}
createFolders(499)