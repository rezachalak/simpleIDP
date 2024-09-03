import React, { useEffect, useState } from 'react';
import api from '../services/api';

interface Cluster {
    id: number;
    name: string;
    status: string;
    is_active: boolean;
    cloud: string;
}

const Clusters: React.FC = () => {
    const [clusters, setClusters] = useState<Cluster[]>([]);

    useEffect(() => {
        api.get<Cluster[]>('clusters/')
            .then(response => {
                setClusters(response.data);
            })
            .catch(error => console.error('Error fetching clusters:', error));
    }, []);

    return (
        <div>
            <h1>Clusters</h1>
            <ul>
                {clusters.map(cluster => (
                    <li key={cluster.id}>
                        {cluster.name} - {cluster.status} - {cluster.is_active ? 'Active' : 'Inactive'}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Clusters;
