import React from 'react'
import './index.css'
import { Header } from './components/header'
import { AddDeliverySection } from './components/addDeliverySection'
import { SavedDeliveriesSection } from './components/savedDeliveriesSection'

function App() {
  const handleSubmit = async ({ trackingNumber, courier }) => {

    try {
      const res = await fetch('https://k70ddit3xh.execute-api.ap-southeast-1.amazonaws.com/track', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ trackingNumber, courier }),
      });
      
      const data = await res.json();
      console.log(data);


      if (!res.ok) {
        alert(data.error);
        throw new Error(data.error);
      }

      console.log('Success:', data);
      alert('Added delivery successfully!');
    } catch (err) {
      console.error('Error submitting tracking info:', err.message);
    }
  };

  return (
    <div className="">
      <Header />
      <div className="flex flex-col items-start max-w-[1450px] py-16 px-48 gap-10">
        <AddDeliverySection onSubmit={handleSubmit} />
        <SavedDeliveriesSection />
      </div>
    </div>
  )
}

export default App