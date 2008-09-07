/***************************************************************************
 SocNetV: Social Networks Visualiser 
 version: 0.44
 Written in Qt 4.4 with KDevelop   
 
                         nodenumber.h  -  description
                             -------------------
    copyright            : (C) 2005-2008 by Dimitris B. Kalamaras
    email                : dimitris.kalamaras@gmail.com
 ***************************************************************************/

/*******************************************************************************
*     This program is free software: you can redistribute it and/or modify     *
*     it under the terms of the GNU General Public License as published by     *
*     the Free Software Foundation, either version 3 of the License, or        *
*     (at your option) any later version.                                      *
*                                                                              *
*     This program is distributed in the hope that it will be useful,          *
*     but WITHOUT ANY WARRANTY; without even the implied warranty of           *
*     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            *
*     GNU General Public License for more details.                             *
*                                                                              *
*     You should have received a copy of the GNU General Public License        *
*     along with this program.  If not, see <http://www.gnu.org/licenses/>.    *
********************************************************************************/

#ifndef NODENUMBER_H
#define NODENUMBER_H

#include <QGraphicsTextItem>

class Node;


static const int TypeNumber=QGraphicsItem::UserType+3;


class NodeNumber : public QGraphicsTextItem {
public:
	NodeNumber(Node * , int, QString,  QGraphicsScene *);
	void removeRefs();
	enum { Type = UserType + 3 };
	int type() const { return Type; }
	~NodeNumber();
  private:
	Node *source;
};

#endif