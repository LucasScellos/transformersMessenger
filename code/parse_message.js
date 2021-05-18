
const fs = require('fs');

let dirs = fs.readdirSync("./inbox");
console.log(dirs);

let jsons = dirs.map((conv) => {
    let files = fs.readdirSync("./inbox/" + conv).filter((file) => file.match("message"));
    let json = null;
    files.forEach(file => {
        if (json == null)
            json = JSON.parse(fs.readFileSync("./inbox/" + conv + "/" + file))
        else {
            let more_json = JSON.parse(fs.readFileSync("./inbox/" + conv + "/" + file));
            json.messages = json.messages.concat(more_json.messages)
        }
    });
    return json;
})
// .filter((json) => json.thread_type == "Regular")
.map((json) => ({messages: json.messages, name: json.title, nb_messages: json.messages.length}))
.sort((a, b) => b.nb_messages - a.nb_messages);


jsons.forEach((json) => console.log({name:json.name, nb:json.nb_messages}));

let types = new Set(['Generic', 'Call', 'Share', 'Unsubscribe']);

let text = jsons[0].messages
.filter((message) => message.type == 'Generic' && message.content != undefined)
.sort((a, b) => a.timestamp_ms - b.timestamp_ms)
.map((message) => `<${message.sender_name}>${message.content}</${message.sender_name}>`)
.join('\n');

fs.writeFileSync("./test.txt", text);