import React from 'react';

export const Header: React.FC = () => {
  return (
    <div className="bg-dark-blue p-10 shadow-lg shadow-grey">
      <div className="flex flex-row items-center max-w-[1450px] mx-auto gap-2">
        <img src="/logo-white.svg" alt="ParcelPal Logo" className="w-auto h-10" />
        <h1 className="text-3xl text-white">
          ParcelExpress
        </h1>
      </div>
    </div>
  )
}