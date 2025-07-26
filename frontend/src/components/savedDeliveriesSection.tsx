import React from 'react';

export const SavedDeliveriesSection: React.FC = () => {
  return (
    <div className="flex flex-col items-start w-full">
      <h1 className="text-3xl font-bold">
        My Deliveries
      </h1>
      <div className="flex flex-row justify-start w-full text-lg mt-4 border-b border-grey pb-2">
        <h1 className="w-3/12">Courier</h1>
        <h1 className="w-4/12">Tracking Number</h1>
        <h1 className="w-3/12">Status</h1>
        <h1 className="w-3/12">Last Update</h1>
      </div>
      <div className="flex flex-row justify-start w-full text-lg mt-4 pb-2">
        <h1 className="w-3/12">Shopee</h1>
        <h1 className="w-4/12">SPXSG053975370797</h1>
        <h1 className="w-3/12">Delivered</h1>
        <h1 className="w-3/12">2023-09-01 10:00:00</h1>
      </div>
    </div>
  )
}