function sendEmail() {
    return new Promise(resolve => {
        setTimeout(() => resolve("Successfully Email sent."), 3000);
    });
}


const emailapp = async (send) => {
    console.log("Email is sending...")
    const res = await send();
    console.log(res);   
}

emailapp(sendEmail)