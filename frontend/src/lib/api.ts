import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function fetchListFriends() {
    try {
        const response = await axios.get(`${API_BASE_URL}/friends`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener la lista de amigos:', error);
        throw error;
    }
}

export async function fetchListBeers() {
    try {
        const response = await axios.get(`${API_BASE_URL}/beers`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener la lista de cervesas:', error);
        throw error;
    }
}

export async function fetchAccountFriend(friend_name: string) {
    try {
        const response = await axios.get(`${API_BASE_URL}/account/${friend_name}`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener la cuenta del amigo escogido:', error);
        throw error;
    }
}