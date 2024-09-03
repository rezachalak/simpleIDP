import React, { useEffect, useState } from 'react';
import api from '../services/api';

interface Cloud {
    id: number;
    name: string;
    provider: string;
    region: string;
    endpoint: string;
}

const Clouds: React.FC = () => {
    const [clouds, setClouds] = useState<Cloud[]>([]);

    useEffect(() => {
        api.get<Cloud[]>('clouds/')
            .then(response => {
                setClouds(response.data);
            })
            .catch(error => console.error('Error fetching clouds:', error));
    }, []);

    return (
        <div>
            <h1>Clouds</h1>
            <ul>
                {clouds.map(cloud => (
                    <li key={cloud.id}>
                        {cloud.name} ({cloud.provider}) - {cloud.region}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Clouds;
