import React, { useState } from 'react';

type AddDeliverySectionProps = {
  onSubmit: (data: { trackingNumber: string; courier: string }) => void;
};

export const AddDeliverySection: React.FC<AddDeliverySectionProps> = ({ onSubmit }) => {
  const couriers = ["Shopee", "NinjaVan", "Lalamove", "GrabExpress"];
  const [courier, setCourier] = useState("Shopee");
  const [trackingNumber, setTrackingNumber] = useState('');

  console.log(courier)

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!courier || !trackingNumber) {
      alert('Please fill in both fields');
      return;
    }

    onSubmit({ trackingNumber, courier });
  };

  return (
    <div className="flex flex-col gap-4 w-full">
      <h1 className="text-3xl font-bold">
        Find My Delivery!
      </h1>
      <div className="flex flex-row w-full gap-2 text-lg">
        <select
          name="courier"
          id="courier"
          value={courier}
          onChange={(e) => setCourier(e.target.value)}
          className="bg-dark-blue text-white rounded-xl w-2/12 shadow-sm p-4 focus:outline-none">
          {couriers.map((courierOption, index) => (
            <option key={index} value={courierOption}>
              {courierOption}
            </option>
          ))}
        </select>
        <input
          type="text"
          value={trackingNumber}
          onChange={(e) => setTrackingNumber(e.target.value)}
          placeholder="Enter your tracking number"
          className="border border-grey rounded-xl w-9/12 p-4 shadow-sm focus:outline-none focus:ring-2 focus:ring-dark-blue"
        />
        <button
          type="submit"
          onClick={handleSubmit}
          className="flex items-center justify-center bg-blue-500 text-white rounded-xl w-1/12 shadow-sm px-4 text-nowrap bg-dark-blue hover:bg-dark-blue-2 transition duration-300"
        >
          <img src="/arrow.svg" alt="Search" className="w-10 h-10" />
        </button>
      </div>
    </div>
  )
}