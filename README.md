# Gold Trading Bot

A Python-based automated trading bot for trading gold (XAUUSD) using MetaTrader 5 (MT5) with technical analysis indicators.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Description
This repository contains a Python script (`gold_bot.py`) that implements an automated trading bot for gold trading on the MetaTrader 5 platform. The bot uses technical indicators like RSI, MACD, Stochastic, Bollinger Bands, and ATR to make trading decisions. It supports both scalping and long-term strategies with risk management features.

## Features
- Real-time market data analysis using MT5.
- Multiple technical indicators for signal generation.
- Scalping and long-term trading strategies.
- Dynamic stop-loss and take-profit calculations.
- Risk management with daily loss limits and position sizing.
- Chart visualization using Plotly.
- Backtesting capabilities.
- Error tracking and email notifications.

## Requirements
- Python 3.13 or higher.
- MetaTrader 5 terminal installed and configured.
- The following Python packages:
  - `MetaTrader5>=5.0.0`
  - `pandas>=1.0.0`
  - `numpy>=1.19.0`
  - `pandas-ta>=0.3.14`
  - `plotly>=5.0.0`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kamaakhona94/inter.git
   cd inter
