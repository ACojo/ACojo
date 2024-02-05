import React, { Component } from 'react';
import { Card, ListGroup } from 'react-bootstrap';
import BasicTable from '../components/BasicTable';

class Statistics extends Component {
    render() {
        return (
            <div>
                <div style={{ justifyContent: 'center', padding: 30 }}>
                    <h2>Statistics Page for the last classification</h2>                 
                    
                </div>
                <div style={{ display: 'flex', justifyContent: 'center', padding: 30 }}>
                    <h2><BasicTable /></h2>
                </div>
            </div>
        );
    }
}

export default Statistics;