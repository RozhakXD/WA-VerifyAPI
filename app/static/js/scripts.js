function capitalizeFirstLetter(text) {
    return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
}

document.getElementById('linkForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const groupLink = document.getElementById('groupLink').value;
    const loading = document.getElementById('loading');
    const message = document.getElementById('message');
    const groupPicture = document.getElementById('groupPicture');
    const floatingMessage = document.getElementById('floatingMessage');
    const floatingMessageText = document.getElementById('floatingMessageText');

    loading.classList.remove('hidden');
    message.textContent = '';
    groupPicture.classList.add('hidden');
    floatingMessage.classList.add('hidden')

    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ link: groupLink }),
        });
        const data = await response.json();
        loading.classList.add('hidden');
        if (data.status === 'success') {
            const groupInfo = data.data.groups_info;
            message.textContent = `Nama Group: ${groupInfo.group_name}`;
            groupPicture.src = groupInfo.profile_picture !== 'null' ? groupInfo.profile_picture : 'https://via.placeholder.com/100';
            groupPicture.alt = `Foto Profil ${groupInfo.group_name}`;
            groupPicture.classList.remove('hidden');
        } else {
            floatingMessageText.textContent = capitalizeFirstLetter(data.message) + '!';
            floatingMessage.classList.remove('hidden');
            floatingMessage.classList.add('show');
            setTimeout(() => {
                floatingMessage.classList.add('hidden');
                floatingMessage.classList.remove('show');
            }, 3000);
        }
    } catch (error) {
        floatingMessageText.textContent = 'Terjadi kesalahan saat memproses permintaan!';
        floatingMessage.classList.remove('hidden');
        floatingMessage.classList.add('show');
        setTimeout(() => {
            floatingMessage.classList.add('hidden');
            floatingMessage.classList.remove('show');
        }, 5000);
    }
});